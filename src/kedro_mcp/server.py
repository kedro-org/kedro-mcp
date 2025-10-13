from pathlib import Path
from fastmcp import FastMCP
from fastmcp.prompts.prompt import PromptMessage, TextContent

mcp = FastMCP("kedro")

# ---------- PROMPT ----------
@mcp.prompt(
    name="convert_notebook",
    description="Convert a Jupyter notebook into a Kedro project."
)
def convert_notebook() -> PromptMessage:
    body = (
        "Call MCP tool `notebook_to_kedro` to load the guidance and follow it.\n"
        "Before executing any CLI commands, check that a virtual environment (venv) is active; "
        "if not, propose creating one.\n"
        "Ensure the latest version of Kedro is installed; install it if missing."
    )
    return PromptMessage(
        role="user",
        content=TextContent(type="text", text=body)
    )

@mcp.prompt(
    name="migration",
    description="Migrate existing project to the latest Kedro version."
)
def migration() -> PromptMessage:
    body = (
        "Call MCP tools `kedro_general_instructions` and `project_migration` to load the guidance.\n"
        "Step 1 — Plan: review the project and suggest a migration plan. Wait for \"APPROVED\".\n"
        "Step 2 — Build: after approval, ensure a virtual environment (venv) is active. "
        "If not, create one. Install Kedro if it is missing, then follow the plan.\n"
        "Keep replies concise."
    )
    return PromptMessage(role="user", content=TextContent(type="text", text=body))

@mcp.prompt(
    name="general_usage",
    description="General usage instructions for Kedro."
)
def general_usage() -> PromptMessage:
    body = (
        "Call MCP tools `kedro_general_instructions` to load the guidance.\n"
        "--- Enter your Kedro-related request here ---"
    )
    return PromptMessage(role="user", content=TextContent(type="text", text=body))


# ---------- DOCS TOOLS ----------
DOCS_ROOT = (Path(__file__).parent / "prompts").resolve()
GENERAL_FILENAME = "kedro_general_instructions.md"
NB2KEDRO_FILENAME = "notebook_to_kedro.md"
MIGRATION_FILENAME = "migration.md"

def _read_doc(filename: str) -> str:
    """Read a doc from prompts/ safely and return its text or a clear error."""
    p = (DOCS_ROOT / filename).resolve()
    # basic containment check
    if not str(p).startswith(str(DOCS_ROOT)):
        return f"⚠️ Illegal path: {filename}"
    if not p.exists():
        return (
            f"⚠️ Could not find '{filename}'.\n"
            f"Expected at: {p}\n\n"
            "Create the file under ./prompts/ or adjust DOCS_ROOT."
        )
    try:
        return p.read_text(encoding="utf-8")
    except Exception as e:
        return f"⚠️ Failed to read '{p}': {e}"

@mcp.tool(name="kedro_general_instructions", description="Return general Kedro usage guidance.")
def kedro_general_instructions() -> str:
    """Return the contents of prompts/kedro_general_instructions.md."""
    return _read_doc(GENERAL_FILENAME)

@mcp.tool(name="notebook_to_kedro", description="Return Notebook→Kedro conversion instructions.")
def notebook_to_kedro() -> str:
    """Return the contents of prompts/notebook_to_kedro.md."""
    return _read_doc(NB2KEDRO_FILENAME)

@mcp.tool(name="project_migration", description="Return project migration instructions.")
def project_migration() -> str:
    """Return the contents of prompts/migration.md."""
    return _read_doc(MIGRATION_FILENAME)

# ---------- ENTRY POINT ----------
def main_stdio():
    print("[kedro-mcp] starting on stdio…", flush=True)
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main_stdio()