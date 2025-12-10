"""
Multi-turn conversation test scenarios.
Used to evaluate chatbot's ability to maintain context and flow.
"""

CONVERSATION_FLOWS = [
    {
        "id": "flow_001",
        "name": "Product Search to Purchase",
        "description": "User searches for product, then wants to buy",
        "turns": [
            {"user": "Show me your monitors", "expected_tool": "list_products"},
            {"user": "Tell me more about the first one", "expected_tool": "get_product"},
            {"user": "I want to buy it", "expected_tool": "verify_customer_pin"},
        ]
    },
    {
        "id": "flow_002",
        "name": "Order Tracking Flow",
        "description": "User checks orders, then asks about specific one",
        "turns": [
            {"user": "Show me my orders", "expected_tool": "list_orders"},
            {"user": "What's the status of the first order?", "expected_tool": "get_order"},
        ]
    },
    {
        "id": "flow_003",
        "name": "Authentication then Order",
        "description": "User verifies identity, then places order",
        "turns": [
            {"user": "I want to place an order", "expected_tool": "verify_customer_pin"},
            {"user": "My email is test@test.com and PIN is 1234", "expected_tool": "verify_customer_pin"},
            {"user": "Order 2 monitors", "expected_tool": "create_order"},
        ]
    },
    {
        "id": "flow_004",
        "name": "Price Comparison",
        "description": "User compares different products",
        "turns": [
            {"user": "Show me printers", "expected_tool": "list_products"},
            {"user": "What about wireless ones?", "expected_tool": "search_products"},
            {"user": "Which is cheaper?", "expected_context": "comparison"},
        ]
    },
    {
        "id": "flow_005",
        "name": "Help and Browse",
        "description": "User asks for help, then browses",
        "turns": [
            {"user": "What can you help me with?", "expected_tool": None},
            {"user": "Show me computers", "expected_tool": "list_products"},
        ]
    },
]

