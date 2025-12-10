"""
AI Agent setup for the Customer Support Chatbot.
"""

from agents import Agent
from src.config import MODEL_NAME, get_logger
from src.prompts import SYSTEM_PROMPT
from src.mcp_client import get_mcp_server

logger = get_logger(__name__)


def create_agent(mcp_server):
    """
    Create a customer support agent with MCP tools.
    
    Args:
        mcp_server: Active MCP server connection
        
    Returns:
        Configured Agent instance
    """
    agent = Agent(
        name="TechStore Support Agent",
        model=MODEL_NAME,
        instructions=SYSTEM_PROMPT,
        mcp_servers=[mcp_server]
    )
    
    logger.info("agent_created", model=MODEL_NAME, name=agent.name)
    return agent


async def run_agent(agent, user_message: str, session:any):
    """
    Run the agent with a user message.
    
    Args:
        agent: The Agent instance
        user_message: User's input message
        context: Optional conversation history
        
    Returns:
        Agent's response string
    """
    from agents import Runner
    
    logger.info("agent_run_start", user_message=user_message[:100])
    
    try:
        # Run the agent
        result = await Runner.run(agent, user_message, session=session)
        
        response = result.final_output
        logger.info("agent_run_success", response_length=len(response))
        
        return response
        
    except Exception as e:
        logger.error("agent_run_error", error=str(e))
        raise

