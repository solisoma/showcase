"""
Unit tests for MCP client connection.
"""

import pytest
import asyncio
from src.mcp_client import get_mcp_server, list_available_tools, test_connection


class TestMCPConnection:
    """Tests for MCP server connection."""
    
    @pytest.mark.asyncio
    async def test_connection_success(self):
        """Test that we can connect to the MCP server."""
        result = await test_connection()
        assert result is True
    
    @pytest.mark.asyncio
    async def test_get_mcp_server_returns_context_manager(self):
        """Test that get_mcp_server returns a valid context manager."""
        mcp = get_mcp_server()
        assert mcp is not None
        # Should be usable as async context manager
        assert hasattr(mcp, '__aenter__')
        assert hasattr(mcp, '__aexit__')
    
    @pytest.mark.asyncio
    async def test_list_tools_returns_tools(self):
        """Test that we can list tools from the MCP server."""
        async with get_mcp_server() as mcp:
            tools = await list_available_tools(mcp)
            assert isinstance(tools, list)
            assert len(tools) > 0
    
    @pytest.mark.asyncio
    async def test_expected_tools_exist(self):
        """Test that all expected tools are available."""
        expected_tools = [
            'list_products',
            'get_product', 
            'search_products',
            'get_customer',
            'verify_customer_pin',
            'list_orders',
            'get_order',
            'create_order'
        ]
        
        async with get_mcp_server() as mcp:
            tools = await list_available_tools(mcp)
            tool_names = [tool.name for tool in tools]
            
            for expected in expected_tools:
                assert expected in tool_names, f"Missing tool: {expected}"

