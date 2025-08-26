import logging
import sys

from .server import mcp

__version__ = "0.0.1.dev0"


def main():
    """Run Kedro MCP server to help AI assistants interact with Kedro"""
    # Configure logging to show warnings by default
    logging.basicConfig(level=logging.WARNING, stream=sys.stderr)

    # Run the MCP server
    mcp.run()


if __name__ == "__main__":
    main()
