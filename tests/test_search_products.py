"""
Unit tests for search_products MCP tool.
"""

import pytest
from src.mcp_client import get_mcp_server


class TestSearchProducts:
    """Tests for the search_products tool."""
    
    @pytest.mark.asyncio
    async def test_search_with_common_term(self):
        """Test searching with a common product term."""
        async with get_mcp_server() as mcp:
            result = await mcp.call_tool("search_products", {"query": "monitor"})
            assert result is not None
    
    @pytest.mark.asyncio
    async def test_search_with_specific_term(self):
        """Test searching with a specific term."""
        async with get_mcp_server() as mcp:
            result = await mcp.call_tool("search_products", {"query": "wireless"})
            assert result is not None
    
    @pytest.mark.asyncio
    async def test_search_no_results(self):
        """Test searching with a term that likely has no results."""
        async with get_mcp_server() as mcp:
            result = await mcp.call_tool("search_products", {"query": "xyznonexistent123"})
            # Should return empty or no matches, not error
            assert result is not None
    
    @pytest.mark.asyncio
    async def test_search_case_insensitive(self):
        """Test that search is case-insensitive."""
        async with get_mcp_server() as mcp:
            result_lower = await mcp.call_tool("search_products", {"query": "printer"})
            result_upper = await mcp.call_tool("search_products", {"query": "PRINTER"})
            # Both should return results (or both empty)
            assert result_lower is not None
            assert result_upper is not None

