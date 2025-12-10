"""
Test cases for customer-related queries.
Used to evaluate chatbot's ability to handle customer authentication and info.
"""

CUSTOMER_TEST_CASES = [
    {
        "id": "cust_001",
        "input": "I need to verify my account",
        "expected_tool": "verify_customer_pin",
        "category": "authentication",
        "description": "Account verification request"
    },
    {
        "id": "cust_002",
        "input": "My email is john@example.com and PIN is 1234",
        "expected_tool": "verify_customer_pin",
        "expected_params": {"email": "john@example.com", "pin": "1234"},
        "category": "authentication",
        "description": "Direct credential provision"
    },
    {
        "id": "cust_003",
        "input": "Look up my account",
        "expected_tool": "verify_customer_pin",
        "category": "account_lookup",
        "description": "Account lookup request"
    },
    {
        "id": "cust_004",
        "input": "What's my shipping address?",
        "expected_tool": "get_customer",
        "category": "info",
        "description": "Customer info request"
    },
    {
        "id": "cust_005",
        "input": "I forgot my PIN",
        "expected_tool": None,
        "category": "support",
        "description": "PIN recovery - no tool, just guidance"
    },
    {
        "id": "cust_006",
        "input": "Verify me: test@company.com 4567",
        "expected_tool": "verify_customer_pin",
        "expected_params": {"email": "test@company.com", "pin": "4567"},
        "category": "authentication",
        "description": "Inline verification format"
    },
    {
        "id": "cust_007",
        "input": "I want to update my address",
        "expected_tool": None,
        "category": "update",
        "description": "Address update - may not be supported"
    },
    {
        "id": "cust_008",
        "input": "Am I a premium customer?",
        "expected_tool": "get_customer",
        "category": "info",
        "description": "Customer role/status query"
    },
]

