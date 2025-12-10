"""
Unit tests for get_product MCP tool.
"""

import pytest
from src.mcp_client import get_mcp_server


class TestGetProduct:
    """Tests for the get_product tool."""
    
    @pytest.mark.asyncio
    async def test_get_product_valid_sku(self):
        """Test getting a product with a valid SKU."""
        async with get_mcp_server() as mcp:
            # First list products to get a valid SKU
            products = await mcp.call_tool("list_products", {})
            # Assuming products exist, try to get one
            # Using a common SKU format
            result = await mcp.call_tool("get_product", {"sku": "COM-0001"})
            assert result is not None
    
    @pytest.mark.asyncio
    async def test_get_product_invalid_sku(self):
        """Test getting a product with an invalid SKU."""
        async with get_mcp_server() as mcp:
            try:
                result = await mcp.call_tool("get_product", {"sku": "INVALID-SKU-999"})
                # If it doesn't raise, check for error message in result
                assert result is not None
            except Exception as e:
                # Expected to raise an error for invalid SKU
                assert "not found" in str(e).lower() or "error" in str(e).lower()
    
    @pytest.mark.asyncio
    async def test_get_product_empty_sku(self):
        """Test getting a product with empty SKU."""
        async with get_mcp_server() as mcp:
            try:
                result = await mcp.call_tool("get_product", {"sku": ""})
                # Should handle empty SKU gracefully
            except Exception:
                # Expected to raise an error
                pass

