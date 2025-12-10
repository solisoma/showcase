"""
Evaluation metrics and scoring for the chatbot.
"""

import asyncio
import time
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime

from src.config import get_logger
from src.mcp_client import get_mcp_server
from src.agent import create_agent, run_agent

logger = get_logger(__name__)


@dataclass
class TestResult:
    """Result of a single test case."""
    test_id: str
    input_text: str
    expected_tool: Optional[str]
    actual_response: str
    response_time_ms: float
    success: bool
    error: Optional[str] = None
    tool_called: Optional[str] = None


@dataclass
class EvaluationReport:
    """Overall evaluation report."""
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    total_tests: int = 0
    passed: int = 0
    failed: int = 0
    accuracy: float = 0.0
    avg_response_time_ms: float = 0.0
    results: List[TestResult] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp,
            "total_tests": self.total_tests,
            "passed": self.passed,
            "failed": self.failed,
            "accuracy": f"{self.accuracy:.2%}",
            "avg_response_time_ms": f"{self.avg_response_time_ms:.2f}",
        }


async def run_single_test(test_case: Dict[str, Any]) -> TestResult:
    """
    Run a single test case against the chatbot.
    
    Args:
        test_case: Dictionary with test case details
        
    Returns:
        TestResult with outcome
    """
    test_id = test_case.get("id", "unknown")
    input_text = test_case.get("input", "")
    expected_tool = test_case.get("expected_tool")
    
    logger.info("test_starting", test_id=test_id)
    
    start_time = time.time()
    
    try:
        async with get_mcp_server() as mcp:
            agent = create_agent(mcp)
            response = await run_agent(agent, input_text)
            
        response_time_ms = (time.time() - start_time) * 1000
        
        # Basic success check - got a response
        success = len(response) > 0
        
        result = TestResult(
            test_id=test_id,
            input_text=input_text,
            expected_tool=expected_tool,
            actual_response=response[:500],  # Truncate for logging
            response_time_ms=response_time_ms,
            success=success,
        )
        
        logger.info("test_completed", test_id=test_id, success=success, response_time_ms=response_time_ms)
        
        return result
        
    except Exception as e:
        response_time_ms = (time.time() - start_time) * 1000
        
        result = TestResult(
            test_id=test_id,
            input_text=input_text,
            expected_tool=expected_tool,
            actual_response="",
            response_time_ms=response_time_ms,
            success=False,
            error=str(e)
        )
        
        logger.error("test_failed", test_id=test_id, error=str(e))
        
        return result


async def run_evaluation(test_cases: List[Dict[str, Any]]) -> EvaluationReport:
    """
    Run evaluation on a list of test cases.
    
    Args:
        test_cases: List of test case dictionaries
        
    Returns:
        EvaluationReport with all results
    """
    report = EvaluationReport()
    report.total_tests = len(test_cases)
    
    logger.info("evaluation_starting", total_tests=report.total_tests)
    
    total_time = 0.0
    
    for test_case in test_cases:
        result = await run_single_test(test_case)
        report.results.append(result)
        
        if result.success:
            report.passed += 1
        else:
            report.failed += 1
        
        total_time += result.response_time_ms
    
    report.accuracy = report.passed / report.total_tests if report.total_tests > 0 else 0.0
    report.avg_response_time_ms = total_time / report.total_tests if report.total_tests > 0 else 0.0
    
    logger.info("evaluation_completed", 
                passed=report.passed, 
                failed=report.failed, 
                accuracy=f"{report.accuracy:.2%}")
    
    return report


def print_report(report: EvaluationReport):
    """Print a formatted evaluation report."""
    print("\n" + "=" * 60)
    print("EVALUATION REPORT")
    print("=" * 60)
    print(f"Timestamp: {report.timestamp}")
    print(f"Total Tests: {report.total_tests}")
    print(f"Passed: {report.passed}")
    print(f"Failed: {report.failed}")
    print(f"Accuracy: {report.accuracy:.2%}")
    print(f"Avg Response Time: {report.avg_response_time_ms:.2f}ms")
    print("=" * 60)
    
    if report.failed > 0:
        print("\nFailed Tests:")
        for result in report.results:
            if not result.success:
                print(f"  - {result.test_id}: {result.error or 'No response'}")
    
    print()


# Example usage
if __name__ == "__main__":
    from metrics.product_queries import PRODUCT_TEST_CASES
    
    async def main():
        # Run subset of tests
        report = await run_evaluation(PRODUCT_TEST_CASES[:3])
        print_report(report)
    
    asyncio.run(main())

