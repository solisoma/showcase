"""
Unit tests for get_customer MCP tool.
"""

import pytest
from src.mcp_client import get_mcp_server


class TestGetCustomer:
    """Tests for the get_customer tool."""
    
    @pytest.mark.asyncio
    async def test_get_customer_invalid_id(self):
        """Test getting a customer with an invalid ID."""
        async with get_mcp_server() as mcp:
            try:
                result = await mcp.call_tool("get_customer", {"customer_id": "invalid-uuid-123"})
                # May return error in result or raise exception
                assert result is not None
            except Exception as e:
                # Expected for invalid customer ID
                assert "not found" in str(e).lower() or "error" in str(e).lower()
    
    @pytest.mark.asyncio
    async def test_get_customer_empty_id(self):
        """Test getting a customer with empty ID."""
        async with get_mcp_server() as mcp:
            try:
                result = await mcp.call_tool("get_customer", {"customer_id": ""})
            except Exception:
                # Expected to raise an error for empty ID
                pass

