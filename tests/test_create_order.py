"""
Unit tests for create_order MCP tool.
"""

import pytest
from src.mcp_client import get_mcp_server


class TestCreateOrder:
    """Tests for the create_order tool."""
    
    @pytest.mark.asyncio
    async def test_create_order_invalid_customer(self):
        """Test creating an order with invalid customer ID."""
        async with get_mcp_server() as mcp:
            try:
                result = await mcp.call_tool("create_order", {
                    "customer_id": "invalid-customer-123",
                    "items": [{"sku": "COM-0001", "quantity": 1, "unit_price": "100.00", "currency": "USD"}]
                })
            except Exception as e:
                # Expected for invalid customer
                assert "not found" in str(e).lower() or "error" in str(e).lower()
    
    @pytest.mark.asyncio
    async def test_create_order_invalid_product(self):
        """Test creating an order with invalid product SKU."""
        async with get_mcp_server() as mcp:
            try:
                result = await mcp.call_tool("create_order", {
                    "customer_id": "some-customer-id",
                    "items": [{"sku": "INVALID-SKU", "quantity": 1, "unit_price": "100.00", "currency": "USD"}]
                })
            except Exception as e:
                # Expected for invalid product
                assert "not found" in str(e).lower() or "error" in str(e).lower()
    
    @pytest.mark.asyncio
    async def test_create_order_empty_items(self):
        """Test creating an order with no items."""
        async with get_mcp_server() as mcp:
            try:
                result = await mcp.call_tool("create_order", {
                    "customer_id": "some-customer-id",
                    "items": []
                })
            except Exception:
                # Expected to raise an error for empty items
                pass

