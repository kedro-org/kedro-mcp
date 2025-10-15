# Kedro MCP Server

An **MCP (Model Context Protocol)** server that helps AI assistants (such as VS Code Copilot or Cursor) work consistently with Kedro projects.

The server provides concise, versioned guidance for:
- General Kedro usage and best practices
- Converting Jupyter notebooks into production-ready Kedro projects
- Migrating projects between Kedro versions

With Kedro-MCP, your AI assistant understands Kedro workflows, pipelines, and conventions — so you can focus on building, not fixing AI mistakes.

---

## Quick Install

To enable Kedro MCP tools in your editor, simply **click one of the links below**.  
Your editor will open automatically, and you’ll just need to confirm installation.

- [**Install in Cursor**](https://cursor.com/en/install-mcp?name=Kedro&config=eyJjb21tYW5kIjoidXZ4IiwiYXJncyI6WyJrZWRyby1tY3BAbGF0ZXN0Il0sImVudiI6eyJGQVNNQ1BfTE9HX0xFVkVMIjoiRVJST1IifSwiZGlzYWJsZWQiOmZhbHNlLCJhdXRvQXBwcm92ZSI6W119)

- [**Install in VS Code**](https://insiders.vscode.dev/redirect/mcp/install?name=Kedro&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22kedro-mcp%40latest%22%5D%2C%22env%22%3A%7B%22FASTMCP_LOG_LEVEL%22%3A%22ERROR%22%7D%2C%22disabled%22%3Afalse%2C%22autoApprove%22%3A%5B%5D%7D)

Once installed, your AI assistant automatically gains access to Kedro-specific MCP tools.

---

### Helpful references

- [VS Code Copilot setup guide](https://code.visualstudio.com/docs/copilot/setup)
- [Cursor quick-start guide](https://cursor.com/docs/get-started/quickstart)

---

### Universal MCP configuration (JSON)

You can reuse this configuration in any MCP-compatible client (e.g. Copilot, Cursor, Claude, Windsurf):

```json
{
  "command": "uvx",
  "args": ["kedro-mcp@latest"],
  "env": {
    "FASTMCP_LOG_LEVEL": "ERROR"
  },
  "disabled": false,
  "autoApprove": []
}
```

---

## Usage

After installation, open **Copilot Chat** (in Agent Mode) or the **Chat panel** in Cursor.  
Type `/` to see available Kedro MCP prompts.

---

### Convert a Jupyter Notebook into a Kedro project

```text
/mcp.Kedro.convert_notebook
```

When you run this command, the assistant explicitly calls the Kedro MCP server and follows the guidance provided.

**Typical flow:**
1. The assistant analyses your Jupyter notebook (you can paste its content or mention its filename).
2. It creates a **conversion plan** (Statement of Work) saved as a `.md` file in your workspace.
3. You review and approve the plan.
4. The assistant:

   - Ensures a Python virtual environment is active.
   - Installs the latest Kedro if missing.
   - Scaffolds a new project with `kedro new`.
   - Creates pipelines with `kedro pipeline create`.
   - Populates `parameters.yml` and `catalog.yml` based on your notebook.

You can edit the plan, switch environment tools (`uv`, `venv`, `conda`), or ask the assistant to resolve setup errors interactively.

---

### Migrate a Kedro project

```text
/mcp.Kedro.project_migration
```

This prompt walks you through migrating an existing Kedro project to a newer version.

**Steps:**
1. The assistant analyses your project and proposes a migration plan (e.g. from 0.19 → 1.0).
2. You review and approve the plan.
3. The assistant ensures a virtual environment is active, installs the correct Kedro version, and applies migration steps.

Use this to get up-to-date migration tips and avoid deprecated patterns.

---

### General Kedro guidance

```text
/mcp.Kedro.general_usage
```

Use this prompt for open-ended Kedro questions.  
The Kedro MCP server returns structured, up-to-date Kedro guidance that your assistant uses to generate realistic code and pipelines.

Example:  
> “Generate a Kedro project for a time-series forecasting pipeline using Pandas and scikit-learn.”

---

## Manual Install (from source)

For development or debugging:

```bash
git clone https://github.com/kedro-org/kedro-mcp.git
cd kedro-mcp
uv pip install -e . --group dev
```

Example MCP config (local path):

```json
{
  "mcpServers": {
    "kedro": {
      "command": "uv",
      "args": ["tool", "run", "--from", ".", "kedro-mcp"],
      "env": { "FASTMCP_LOG_LEVEL": "ERROR" }
    }
  }
}
```

---

## Development

```bash
# Install dev dependencies
uv pip install -e . --group dev

# Lint & type-check
ruff check .
mypy src/
```

---

## Troubleshooting

- **Server not starting:** Ensure Python 3.10+ and `uv` are installed. Confirm the MCP config points to `uvx kedro-mcp@latest` or to the `kedro-mcp` console script.
- **Tools not appearing:** Restart your assistant and verify that the MCP config key matches `"kedro"`.
- **Version drift:** Pin a version instead of `@latest` for reproducibility.

---

## License

This project is licensed under the **Apache Software License 2.0**.  
See `LICENSE.txt` for details.

---

## Support

- Report issues: [https://github.com/kedro-org/kedro-mcp/issues](https://github.com/kedro-org/kedro-mcp/issues)  
- Learn more about MCP: [https://modelcontextprotocol.io/](https://modelcontextprotocol.io/)
