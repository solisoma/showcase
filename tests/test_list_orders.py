"""
Unit tests for list_orders MCP tool.
"""

import pytest
from src.mcp_client import get_mcp_server


class TestListOrders:
    """Tests for the list_orders tool."""
    
    @pytest.mark.asyncio
    async def test_list_all_orders(self):
        """Test listing all orders without filters."""
        async with get_mcp_server() as mcp:
            result = await mcp.call_tool("list_orders", {})
            assert result is not None
    
    @pytest.mark.asyncio
    async def test_list_orders_by_status(self):
        """Test filtering orders by status."""
        async with get_mcp_server() as mcp:
            result = await mcp.call_tool("list_orders", {"status": "submitted"})
            assert result is not None
    
    @pytest.mark.asyncio
    async def test_list_orders_invalid_status(self):
        """Test with an invalid status filter."""
        async with get_mcp_server() as mcp:
            result = await mcp.call_tool("list_orders", {"status": "invalid_status"})
            # Should handle gracefully
            assert result is not None
    
    @pytest.mark.asyncio
    async def test_list_orders_by_customer(self):
        """Test filtering orders by customer ID."""
        async with get_mcp_server() as mcp:
            result = await mcp.call_tool("list_orders", {"customer_id": "some-uuid"})
            # May return empty if customer doesn't exist
            assert result is not None

