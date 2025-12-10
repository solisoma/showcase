"""
Unit tests for AI Agent.
"""

import pytest
from src.mcp_client import get_mcp_server
from src.agent import create_agent, run_agent


class TestAgent:
    """Tests for the AI Agent."""
    
    @pytest.mark.asyncio
    async def test_agent_creation(self):
        """Test that agent can be created with MCP server."""
        async with get_mcp_server() as mcp:
            agent = create_agent(mcp)
            assert agent is not None
            assert agent.name == "TechStore Support Agent"
    
    @pytest.mark.asyncio
    async def test_agent_responds_to_greeting(self):
        """Test that agent responds to a simple greeting."""
        async with get_mcp_server() as mcp:
            agent = create_agent(mcp)
            response = await run_agent(agent, "Hello!")
            assert response is not None
            assert len(response) > 0
    
    @pytest.mark.asyncio
    async def test_agent_uses_tools_for_product_query(self):
        """Test that agent uses tools when asked about products."""
        async with get_mcp_server() as mcp:
            agent = create_agent(mcp)
            response = await run_agent(agent, "What products do you have?")
            assert response is not None
            assert len(response) > 0
    
    @pytest.mark.asyncio
    async def test_agent_handles_search_query(self):
        """Test that agent handles product search queries."""
        async with get_mcp_server() as mcp:
            agent = create_agent(mcp)
            response = await run_agent(agent, "Search for monitors")
            assert response is not None
            assert len(response) > 0

