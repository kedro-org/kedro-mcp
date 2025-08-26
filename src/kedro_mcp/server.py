"""FastMCP server setup (Uvx or CLI entrypoint) exposing all available tools and prompts"""

from mcp.server.fastmcp import FastMCP  

mcp = FastMCP(
    "MCP server to help AI assistants interact with Kedro",
)

@mcp.tool(title="Health Check")
def health_check() -> dict:
    """
    Simple health check tool to verify MCP server is running.
    Returns basic metadata about the server.
    """
    return {
        "status": "ok",
        "message": "kedro-mcp server is up and running 🚀",
        "version": "0.0.1.dev0",
    }
