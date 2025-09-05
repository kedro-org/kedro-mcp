"""FastMCP server setup (Uvx or CLI entrypoint) exposing all available tools and prompts"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "MCP server to help AI assistants interact with Kedro",
)

@mcp.prompt(title="Kedro Assistant Guidance")
def kedro_guidance() -> str:
    """
    Guidance for AI assistants when helping with Kedro-related questions.
    """
    return """
    When helping users with Kedro-related questions, always refer to the comprehensive Kedro documentation first.
    
    **Key Documentation Resources:**
    - For Kedro framework documentation, see: https://docs.kedro.org/en/stable/llm.txt
    - For comprehensive kedro-dataset documentation, see: https://docs.kedro.org/projects/kedro-datasets/en/stable/llms.txt  
    - For pipeline visualisation documentation, see: https://docs.kedro.org/projects/kedro-viz/en/stable/llms.txt
    
    Always check these resources when users ask about:
    - Kedro project setup, configuration, or best practices
    - Data catalogs, datasets, or data loading/saving
    - Pipeline creation, visualization, or deployment
    - Kedro plugins, extensions, or integrations
    """

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

@mcp.tool(title="Get Kedro Documentation")
def get_kedro_documentation() -> dict:
    """
    Get Kedro documentation links for comprehensive information.
    
    Returns:
        Dictionary with links to Kedro documentation resources for LLMs.
    """
    return {
        "message": "For comprehensive Kedro documentation, please read the following resources:",
        "documentation_links": {
            "kedro": "https://docs.kedro.org/en/stable/llm.txt",
            "kedro_datasets": "https://docs.kedro.org/projects/kedro-datasets/en/stable/llms.txt", 
            "kedro_viz": "https://docs.kedro.org/projects/kedro-viz/en/stable/llms.txt"
        },
        "instructions": [
            "For Kedro framework documentation, see: https://docs.kedro.org/en/stable/llm.txt",
            "For comprehensive kedro-dataset documentation, see: https://docs.kedro.org/projects/kedro-datasets/en/stable/llms.txt",
            "For pipeline visualisation documentation, see: https://docs.kedro.org/projects/kedro-viz/en/stable/llms.txt",
        ]
    }
