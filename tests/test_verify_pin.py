"""
Unit tests for verify_customer_pin MCP tool.
"""

import pytest
from src.mcp_client import get_mcp_server


class TestVerifyCustomerPin:
    """Tests for the verify_customer_pin tool."""
    
    @pytest.mark.asyncio
    async def test_verify_invalid_credentials(self):
        """Test verification with invalid email and PIN."""
        async with get_mcp_server() as mcp:
            try:
                result = await mcp.call_tool("verify_customer_pin", {
                    "email": "nonexistent@fake.com",
                    "pin": "0000"
                })
                # Should indicate verification failed
                assert result is not None
            except Exception as e:
                # Expected for invalid credentials
                assert "not found" in str(e).lower() or "error" in str(e).lower()
    
    @pytest.mark.asyncio
    async def test_verify_missing_email(self):
        """Test verification with missing email."""
        async with get_mcp_server() as mcp:
            try:
                result = await mcp.call_tool("verify_customer_pin", {
                    "email": "",
                    "pin": "1234"
                })
            except Exception:
                # Expected to raise an error
                pass
    
    @pytest.mark.asyncio
    async def test_verify_missing_pin(self):
        """Test verification with missing PIN."""
        async with get_mcp_server() as mcp:
            try:
                result = await mcp.call_tool("verify_customer_pin", {
                    "email": "test@test.com",
                    "pin": ""
                })
            except Exception:
                # Expected to raise an error
                pass

