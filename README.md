# Kedro MCP Server

An MCP (Model Context Protocol) server that helps AI assistants work consistently with Kedro projects.  
It ships a tiny prompt and two read-only tools that return concise, versioned guidance for general Kedro usage and for converting a Jupyter notebook into a production-ready Kedro project.

---

## ⚡ Quick Install

- [**Install in Cursor**](https://cursor.com/en/install-mcp?name=Kedro&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22kedro-mcp%40latest%22%5D%2C%22env%22%3A%7B%22FASTMCP_LOG_LEVEL%22%3A%22ERROR%22%7D%2C%22disabled%22%3Afalse%2C%22autoApprove%22%3A%5B%5D%7D)

- [**Install in VS Code**](https://insiders.vscode.dev/redirect/mcp/install?name=Kedro&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22kedro-mcp%40latest%22%5D%2C%22env%22%3A%7B%22FASTMCP_LOG_LEVEL%22%3A%22ERROR%22%7D%2C%22disabled%22%3Afalse%2C%22autoApprove%22%3A%5B%5D%7D)

Once installed, your AI assistant automatically gains access to Kedro-specific MCP tools.

---

## 🛠️ Examples of Usage

After installing, open **Copilot Chat** (VS Code) or the **Chat panel** (Cursor).  
Type `/` to see available MCP prompts.

### Example 1 — Notebook → Kedro Project
```text
/mcp.Kedro.convert_notebook
```
Your assistant will propose a **step-by-step plan** to convert a Jupyter Notebook into a production-ready Kedro project:
- Create a project scaffold with `kedro new`
- Define pipelines with `kedro pipeline create`
- Populate `parameters.yml` and `catalog.yml`

---

### Example 2 — Kedro Migration
```text
/mcp.Kedro.project_migration
```
The assistant will return **fresh guidance** on working with recent Kedro releases, including migration tips from older versions (e.g., 0.19 → 1.0).

---

### Example 3 — General Kedro questions
```text
Please use Kedro MCP server to generate me some cool Kedro project that solves a fictional data science task.
```
You can ask your AI assistant open-ended Kedro questions.  
The Kedro MCP server provides scaffolding instructions and conventions so the assistant generates realistic Kedro pipelines and structures — even for hypothetical projects.

---

## 🛠️ Manual Install (from source)

For development or debugging:

```bash
git clone https://github.com/kedro-org/kedro-mcp.git
cd kedro-mcp
uv pip install -e . --group dev
```

Config (local path):
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
# Install dev deps
uv pip install -e . --group dev

# Lint & type-check
ruff check .
mypy src/
```

---

## Troubleshooting

- **Server not starting**: ensure Python 3.10+ and `uv` are installed; confirm the MCP config points to `uvx kedro-mcp@latest` or to the `kedro-mcp` console script.
- **Tools don’t appear**: restart the assistant; verify the MCP config key matches `"kedro"` and the client supports stdio servers.
- **Version drift**: pin a version instead of `@latest`.

---

## License

This project is licensed under the Apache Software License 2.0. See `LICENSE.txt` for details.

---

## Support

- Report issues: https://github.com/kedro-org/kedro-mcp/issues  
- MCP specification: https://modelcontextprotocol.io/
