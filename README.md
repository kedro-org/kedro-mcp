# Kedro MCP Server

An MCP (Model Context Protocol) server that helps AI assistants work consistently with Kedro projects.  
It ships a tiny prompt and two read-only tools that return concise, versioned guidance for general Kedro usage and for converting a Jupyter notebook into a production-ready Kedro project.

---

## 🚀 Quick install (no setup, runs locally)

**Prerequisites**
- Python 3.10+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (recommended)

**VS Code – GitHub Copilot Chat (user or workspace settings):**
```jsonc
{
  "github.copilot.chat.mcpServers": {
    "kedro": {
      "type": "stdio",
      "command": "uvx",
      "args": ["kedro-mcp@latest"],   // or pin: kedro-mcp==0.1.0
      "env": { "FASTMCP_LOG_LEVEL": "ERROR" },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

**Claude Desktop / Cursor (generic MCP config):**
```json
{
  "mcpServers": {
    "kedro": {
      "command": "uvx",
      "args": ["kedro-mcp@latest"],
      "env": { "FASTMCP_LOG_LEVEL": "ERROR" },
      "disabled": false
    }
  }
}
```

Now open your assistant and ask:
- “Call `kedro_general_instructions` and summarise the key conventions.”
- “Call `notebook_to_kedro`, propose a short plan for my notebook. Wait for **APPROVED**.”

> Tip: `@latest` auto-refreshes when a newer version is released. Pin a version to freeze behaviour.


---

## Features

- **Prompt**
  - `convert_notebook` – a short, plain-English prompt that tells the assistant to:
    1) load both guidance docs via tools,
    2) return a brief conversion plan and wait for **APPROVED**,
    3) then create the Kedro project (venv, install Kedro first), without running pipelines or moving data.

- **Tools (read-only)**
  - `kedro_general_instructions` – returns concise conventions for consistent Kedro usage (naming, datasets, parameters, environments, checklists).
  - `notebook_to_kedro` – returns focused guidance for notebook → Kedro conversion (plan → approval → build) with small templates/diffs.

Both tools just return Markdown text for the assistant to use as context; they **do not** read your files or send project data anywhere.

---

## Installation

### Option A — Zero-install (recommended)
Nothing to install into your environment. Your MCP client will run the server locally via `uvx` using the config above. First run is cached; later runs reuse the cache and only update when you use `@latest` or change the version.

### Option B — From PyPI (when available)
```bash
uv pip install kedro-mcp
```
Then point your client to the console script:
```json
{
  "mcpServers": {
    "kedro": { "command": "kedro-mcp", "args": [] }
  }
}
```

### Option C — From source (local development)
```bash
git clone https://github.com/kedro-org/kedro-mcp.git
cd kedro-mcp
uv pip install -e . --group dev
```
Config for local path:
```json
{
  "mcpServers": {
    "kedro": {
      "command": "uv",
      "args": ["tool","run","--from",".","kedro-mcp"]
    }
  }
}
```

---

## Manual server test

```bash
# Runs the stdio entrypoint (the client usually does this for you)
kedro-mcp

# Or with uvx directly (no install)
uvx kedro-mcp@latest
```

You should see a small “starting on stdio…” log; then your client will communicate over stdio.

---

## Using with assistants

- **VS Code – Copilot Chat**: once configured, the server and tools appear automatically; you can invoke them by name in chat.
- **Claude Desktop / Cursor**: add the generic MCP config above; the tools can be called by name (e.g., `notebook_to_kedro`).

Suggested prompts:
- “Call `kedro_general_instructions`, then summarise conventions that are missing in this repo.”
- “Call `notebook_to_kedro`, propose a conversion plan for `analysis.ipynb`. Wait for **APPROVED** before creating anything.”

---

## Development

```bash
# Install dev deps
uv pip install -e . --group dev

# Lint & type-check
ruff check .
mypy src/
```

### Releasing
```bash
python -m pip install build twine
python -m build
twine upload dist/*
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
