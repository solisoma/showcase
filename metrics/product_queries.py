"""
Test cases for product-related queries.
Used to evaluate chatbot's ability to handle product inquiries.
"""

PRODUCT_TEST_CASES = [
    {
        "id": "prod_001",
        "input": "What products do you have?",
        "expected_tool": "list_products",
        "category": "browse",
        "description": "General product browsing request"
    },
    {
        "id": "prod_002", 
        "input": "Show me all monitors",
        "expected_tool": "list_products",
        "expected_params": {"category": "Monitors"},
        "category": "browse_filtered",
        "description": "Product browsing with category filter"
    },
    {
        "id": "prod_003",
        "input": "What printers do you sell?",
        "expected_tool": "list_products",
        "expected_params": {"category": "Printers"},
        "category": "browse_filtered",
        "description": "Printer category query"
    },
    {
        "id": "prod_004",
        "input": "Search for wireless printer",
        "expected_tool": "search_products",
        "expected_params": {"query": "wireless printer"},
        "category": "search",
        "description": "Keyword search for products"
    },
    {
        "id": "prod_005",
        "input": "Do you have any 4K monitors?",
        "expected_tool": "search_products",
        "expected_params": {"query": "4K"},
        "category": "search",
        "description": "Specific feature search"
    },
    {
        "id": "prod_006",
        "input": "Tell me about product COM-0001",
        "expected_tool": "get_product",
        "expected_params": {"sku": "COM-0001"},
        "category": "detail",
        "description": "Product detail by SKU"
    },
    {
        "id": "prod_007",
        "input": "What's the price of SKU MON-0054?",
        "expected_tool": "get_product",
        "expected_params": {"sku": "MON-0054"},
        "category": "detail",
        "description": "Price inquiry by SKU"
    },
    {
        "id": "prod_008",
        "input": "Is the gaming monitor in stock?",
        "expected_tool": "search_products",
        "expected_params": {"query": "gaming monitor"},
        "category": "availability",
        "description": "Stock availability query"
    },
    {
        "id": "prod_009",
        "input": "I need a computer under $1000",
        "expected_tool": "search_products",
        "expected_params": {"query": "computer"},
        "category": "search_with_constraint",
        "description": "Product search with price constraint"
    },
    {
        "id": "prod_010",
        "input": "Show me your cheapest printer",
        "expected_tool": "list_products",
        "expected_params": {"category": "Printers"},
        "category": "comparative",
        "description": "Comparative product query"
    },
]

