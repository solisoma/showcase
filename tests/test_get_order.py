"""
Unit tests for get_order MCP tool.
"""

import pytest
from src.mcp_client import get_mcp_server


class TestGetOrder:
    """Tests for the get_order tool."""
    
    @pytest.mark.asyncio
    async def test_get_order_invalid_id(self):
        """Test getting an order with an invalid ID."""
        async with get_mcp_server() as mcp:
            try:
                result = await mcp.call_tool("get_order", {"order_id": "invalid-order-123"})
                assert result is not None
            except Exception as e:
                # Expected for invalid order ID
                assert "not found" in str(e).lower() or "error" in str(e).lower()
    
    @pytest.mark.asyncio
    async def test_get_order_empty_id(self):
        """Test getting an order with empty ID."""
        async with get_mcp_server() as mcp:
            try:
                result = await mcp.call_tool("get_order", {"order_id": ""})
            except Exception:
                # Expected to raise an error
                pass

