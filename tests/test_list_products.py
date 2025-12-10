"""
Unit tests for list_products MCP tool.
"""

import pytest
from src.mcp_client import get_mcp_server


class TestListProducts:
    """Tests for the list_products tool."""
    
    @pytest.mark.asyncio
    async def test_list_all_products(self):
        """Test listing all products without filters."""
        async with get_mcp_server() as mcp:
            result = await mcp.call_tool("list_products", {})
            assert result is not None
            # Should return some product data
            assert len(str(result)) > 0
    
    @pytest.mark.asyncio
    async def test_list_products_by_category(self):
        """Test filtering products by category."""
        async with get_mcp_server() as mcp:
            result = await mcp.call_tool("list_products", {"category": "Monitors"})
            assert result is not None
    
    @pytest.mark.asyncio
    async def test_list_active_products_only(self):
        """Test filtering for active products only."""
        async with get_mcp_server() as mcp:
            result = await mcp.call_tool("list_products", {"is_active": True})
            assert result is not None
    
    @pytest.mark.asyncio
    async def test_list_products_with_invalid_category(self):
        """Test with a category that may not exist."""
        async with get_mcp_server() as mcp:
            result = await mcp.call_tool("list_products", {"category": "NonExistentCategory123"})
            # Should not raise an error, just return empty or no matches
            assert result is not None

