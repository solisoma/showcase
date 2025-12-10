"""
Test cases for order-related queries.
Used to evaluate chatbot's ability to handle order inquiries and creation.
"""

ORDER_TEST_CASES = [
    {
        "id": "ord_001",
        "input": "Show me my orders",
        "expected_tool": "list_orders",
        "category": "list",
        "description": "General order list request"
    },
    {
        "id": "ord_002",
        "input": "Where is my order?",
        "expected_tool": "list_orders",
        "category": "tracking",
        "description": "Order tracking query"
    },
    {
        "id": "ord_003",
        "input": "What's the status of order ORD-12345?",
        "expected_tool": "get_order",
        "expected_params": {"order_id": "ORD-12345"},
        "category": "detail",
        "description": "Specific order status query"
    },
    {
        "id": "ord_004",
        "input": "Show me my pending orders",
        "expected_tool": "list_orders",
        "expected_params": {"status": "submitted"},
        "category": "list_filtered",
        "description": "Orders filtered by status"
    },
    {
        "id": "ord_005",
        "input": "I want to place an order",
        "expected_tool": "verify_customer_pin",
        "category": "create_intent",
        "description": "Order creation intent - should verify first"
    },
    {
        "id": "ord_006",
        "input": "I'd like to buy 2 monitors",
        "expected_tool": "verify_customer_pin",
        "category": "create_intent",
        "description": "Purchase intent - should verify first"
    },
    {
        "id": "ord_007",
        "input": "Add a printer to my cart",
        "expected_tool": "search_products",
        "category": "pre_order",
        "description": "Cart addition - may search first"
    },
    {
        "id": "ord_008",
        "input": "What did I order last time?",
        "expected_tool": "list_orders",
        "category": "history",
        "description": "Order history query"
    },
    {
        "id": "ord_009",
        "input": "Cancel my order",
        "expected_tool": "get_order",
        "category": "cancellation",
        "description": "Order cancellation request"
    },
    {
        "id": "ord_010",
        "input": "Is my order shipped yet?",
        "expected_tool": "list_orders",
        "category": "tracking",
        "description": "Shipping status query"
    },
]

