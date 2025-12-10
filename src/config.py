"""
Configuration settings for the Customer Support Chatbot.
"""

import os
import logging
import structlog
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

# =============================================================================
# API CONFIGURATION
# =============================================================================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MCP_SERVER_URL = os.getenv("ALLIANCE_MCP_SERVER", "https://vipfapwm3x.us-east-1.awsapprunner.com/mcp")

# =============================================================================
# MODEL CONFIGURATION
# =============================================================================

MODEL_NAME = "gpt-4o-mini"  # Cheap and fast
MODEL_TEMPERATURE = 0.7
MCP_TIMEOUT = 50

# =============================================================================
# APPLICATION SETTINGS
# =============================================================================

APP_TITLE = "TechStore Customer Support"
APP_DESCRIPTION = "AI-powered support for monitors, printers, and computer products"

# =============================================================================
# LOGGING CONFIGURATION
# =============================================================================

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_DIR = "logs"

def setup_logging():
    """Configure structured logging with structlog."""
    
    # Create logs directory if it doesn't exist
    os.makedirs(LOG_DIR, exist_ok=True)
    
    # Configure structlog
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.JSONRenderer()
        ],
        wrapper_class=structlog.stdlib.BoundLogger,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )
    
    # Set up standard logging
    logging.basicConfig(
        format="%(message)s",
        level=getattr(logging, LOG_LEVEL.upper()),
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(f"{LOG_DIR}/app.log")
        ]
    )

def get_logger(name: str):
    """Get a structured logger instance."""
    return structlog.get_logger(name)

# =============================================================================
# VALIDATION
# =============================================================================

def validate_config():
    """Validate that all required configuration is present."""
    errors = []
    
    if not OPENAI_API_KEY:
        errors.append("OPENAI_API_KEY is not set")
    
    if not MCP_SERVER_URL:
        errors.append("ALLIANCE_MCP_SERVER is not set")
    
    if errors:
        raise ValueError(f"Configuration errors: {', '.join(errors)}")
    
    return True

