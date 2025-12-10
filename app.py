"""
TechStore Customer Support Chatbot
Main entry point for the Gradio application.
"""

from src.config import setup_logging, validate_config, get_logger
from src.mcp_client import get_mcp_server
from src.agent import create_agent, run_agent
from src.ui import create_chat_interface, launch_ui
import asyncio

# Initialize logging
setup_logging()
logger = get_logger(__name__)


async def main():
    """Main entry point."""
    logger.info("app_starting")
    
    # Validate configuration before starting
    validate_config()
    logger.info("config_validated")
    
    async with get_mcp_server() as mcp:
        agent = create_agent(mcp)

        async def chat_handler(message: str, history: list) -> str:
            """
            Reuses persistent connection" for accuracy
            """
            try:
                response = await run_agent(agent, message)
                return response
            except Exception as e:
                logger.error("chat_handler_error", error=str(e))
                return f"I apologize, but I encountered an error. Please try again. Error: {str(e)}"
        demo = create_chat_interface(chat_handler)
        launch_ui(demo, share=False)

if __name__ == "__main__":
    asyncio.run(main())

