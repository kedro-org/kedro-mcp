import asyncio
import logging
import sys

from kedro_mcp.server import mcp

__version__ = "0.0.1.dev0"

logger = logging.getLogger(__name__)

def main() -> None:
    """Run Kedro MCP server to help AI assistants interact with Kedro"""
    # Configure logging to show warnings by default
    logging.basicConfig(level=logging.WARNING, stream=sys.stderr)

    logger.info("✅ Starting Kedro-MCP server...")
    logger.info("Available tools: %s", asyncio.run(mcp.list_tools()))

    # Run the MCP server
    mcp.run()


if __name__ == "__main__":
    main()
