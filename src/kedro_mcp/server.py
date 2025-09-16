from pathlib import Path
from fastmcp import FastMCP
from fastmcp.prompts.prompt import PromptMessage, TextContent

mcp = FastMCP("kedro")

# ---------- PROMPT ----------
@mcp.prompt(
    name="convert_notebook",
    description="Convert a Jupyter notebook into a production-ready Kedro project (plan → approval → build)."
)
def convert_notebook() -> PromptMessage:
    body = (
        "Call MCP tools `kedro_general_instructions` and `notebook_to_kedro` to load the guidance.\n"
        "Step 1 — Plan: read the notebook and return a short conversion plan. Wait for \"APPROVED\".\n"
        "Step 2 — Build: after approval, use a virtual environment (venv) and install Kedro before running any Kedro commands; then create the Kedro project as in the docs. Do not run the pipeline or move data.\n"
        "Keep replies concise."
    )
    return PromptMessage(role="user", content=TextContent(type="text", text=body))

# ---------- DOCS TOOLS ----------
DOCS_ROOT = (Path(__file__).parent / "prompts").resolve()
GENERAL_FILENAME = "kedro_general_instructions.md"
NB2KEDRO_FILENAME = "notebook_to_kedro.md"

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

# ---------- ENTRY POINT ----------
def main_stdio():
    print("[kedro-mcp] starting on stdio…", flush=True)
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main_stdio()