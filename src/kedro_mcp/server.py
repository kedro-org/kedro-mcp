"""FastMCP server setup (Uvx or CLI entrypoint) exposing all available tools and prompts"""

from mcp.server.fastmcp import FastMCP

from kedro_mcp.schemas.catalog.base_schemas import CatalogFindingsSchema
from kedro_mcp.utils.catalog_utils import validate_project_catalog

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


@mcp.tool(title="Validate Kedro DataCatalog")
def validate_catalog() -> CatalogFindingsSchema:
    """Validates Kedro DataCatalog YAMLs in the project and returns findings."""
    return validate_project_catalog()
