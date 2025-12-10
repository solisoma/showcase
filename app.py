"""
TechStore Customer Support Chatbot
Main entry point for the Gradio application.
"""

from uuid import uuid4
from src.config import setup_logging, validate_config, get_logger
from src.mcp_client import get_mcp_server
from src.agent import create_agent, run_agent
from agents import SQLiteSession
from src.ui import create_chat_interface, launch_ui

# Initialize logging
setup_logging()
logger = get_logger(__name__)


def main():
    """Main entry point."""
    logger.info("app_starting")
    
    # Validate configuration before starting
    validate_config()
    logger.info("config_validated")

    session = SQLiteSession(uuid4().hex)
    
    # Chat handler - creates MCP connection per request
    async def chat_handler(message: str, history: list) -> str:
        """
        Handle incoming chat messages.
        Creates fresh MCP connection and agent for each request.
        """
        try:
            async with get_mcp_server() as mcp:
                agent = create_agent(mcp)
                response = await run_agent(agent, message, session)
                return response
        except Exception as e:
            logger.error("chat_handler_error", error=str(e))
            return f"I apologize, but I encountered an error. Please try again. Error: {str(e)}"
    
    # Create and launch the UI
    demo = create_chat_interface(chat_handler)
    launch_ui(demo, share=False)


if __name__ == "__main__":
    main()
