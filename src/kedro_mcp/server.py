"""FastMCP server setup (Uvx or CLI entrypoint) exposing all available tools and prompts"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "MCP server to help AI assistants interact with Kedro",
)
