"""
MCP Client wrapper for connecting to the company's backend server.
"""

import os
from agents.mcp import MCPServerStreamableHttp
from src.config import MCP_SERVER_URL, MCP_TIMEOUT, get_logger

logger = get_logger(__name__)

# MCP connection parameters
MCP_PARAMS = {
    "url": MCP_SERVER_URL,
    "timeout": MCP_TIMEOUT
}

def get_mcp_server():
    """
    Get an MCP server instance.
    
    Usage:
        async with get_mcp_server() as mcp:
            tools = await mcp.list_tools()
    
    Returns:
        MCPServerStreamableHttp instance
    """
    logger.info("mcp_connection_init", url=MCP_SERVER_URL)
    return MCPServerStreamableHttp(params=MCP_PARAMS)


async def list_available_tools(mcp):
    """
    List all available tools from the MCP server.
    
    Args:
        mcp: Active MCP server connection
        
    Returns:
        List of tool objects
    """
    tools = await mcp.list_tools()
    logger.info("tools_listed", count=len(tools))
    return tools


async def test_connection():
    """
    Test the MCP server connection.
    
    Returns:
        True if connection successful, raises exception otherwise
    """
    async with get_mcp_server() as mcp:
        tools = await mcp.list_tools()
        logger.info("connection_test_success", tools_count=len(tools))
        return True

