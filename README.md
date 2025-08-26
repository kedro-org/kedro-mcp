# Kedro MCP Server

An MCP (Model Context Protocol) server that helps AI assistants interact with Kedro projects. This server provides tools and capabilities to work with Kedro data catalogs, pipelines, and project structures through various AI coding assistants.

## Project Structure

```
kedro-mcp/
├── LICENSE.txt
├── README.md
├── pyproject.toml
├── docs/
├── src/
│   └── kedro_mcp/
│       ├── __init__.py
│       ├── server.py           # Main MCP server implementation
│       ├── schemas/
│       │   ├── __init__.py
│       │   └── catalog_schemas.py
│       └── utils/
│           ├── __init__.py
│           └── catalog_utils.py
└── tests/
```

## Installation

### Prerequisites

- Python 3.10 or higher
- Kedro 1.0.0 or higher
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (recommended)

### Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install from Source

1. Clone the repository:
```bash
git clone https://github.com/kedro-org/kedro-mcp.git
cd kedro-mcp
```

2. Install the package:
```bash
uv pip install -e .
```

### Install from PyPI (when available)
```bash
uv pip install kedro-mcp
```

## Development Setup

**Note**: This project requires [uv](https://docs.astral.sh/uv/) for dependency management to support modern dependency groups.

1. Install uv if you haven't already:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# Or: pip install uv
```

2. Install the package and development dependencies:
```bash
uv pip install -e . --group dev
```

3. Run linting and type checking:
```bash
ruff check .
mypy src/
```

## Integration with AI Assistants

### VS Code

Once you have uv, and have installed Visual Studio Code, you need to set up the Kedro-MCP server configuration.

1. Open VS Code
2. Add the MCP server configuration in your workspace settings (`.vscode/mcp.json`):

**For published package:**

If you've installed uv, open a terminal window and type uv to confirm that is available. To get the path to uvx, type the following:

```
which uvx
```

Now configure the workspace settings:

```json
{
  "servers": {
    "kedro-mcp": {
      "command": "/placeholder-path/uvx",
      "args": ["kedro-mcp"]
    }
  }
}
```

**For local development:**

```json
{
  "servers": {
    "kedro-mcp": {
      "command": "/path/to/your/venv/bin/kedro-mcp",
      "args": []
    }
  }
}
```

OR

**Using uv:**

```json
{
  "servers": {
    "kedro-mcp": {
      "command": "<full-path-to-your-uv-executable>",
      "args": [
        "run",
        "--directory",
        "<full-path-to-your-kedro-mcp-dir>",
        "kedro-mcp"
      ]
    }
  }
}
```

3. Restart VS Code (optional)
4. The Kedro MCP server will be available with tools like `health_check`

### GitHub Copilot Chat Integration

- Once VS Code integration is successful, copilot chat will automatically identify available MCP servers. Follow [this](https://code.visualstudio.com/docs/copilot/customization/mcp-servers#_view-installed-mcp-servers) for more information.
- Follow [this](https://code.visualstudio.com/docs/copilot/customization/mcp-servers#_use-mcp-tools-in-agent-mode) to use MCP tools in agent mode.


### Claude Desktop Integration

1. Open Claude Desktop settings and go to Developer settings (Edit Config to add and manage MCP servers)
2. Add the MCP server configuration:

**For published package:**

```json
{
  "mcpServers": {
    "kedro-mcp": {
      "command": "/placeholder-path/uvx",
      "args": ["kedro-mcp"]
    }
  }
}
```

**For local development:**

```json
{
  "mcpServers": {
    "kedro-mcp": {
      "command": "/path/to/your/venv/bin/kedro-mcp",
      "args": []
    }
  }
}
```

OR

**Using uv:**

```json
{
  "servers": {
    "kedro-mcp": {
      "command": "<full-path-to-your-uv-executable>",
      "args": [
        "run",
        "--directory",
        "<full-path-to-your-kedro-mcp-dir>",
        "kedro-mcp"
      ]
    }
  }
}
```

3. Restart Claude Desktop
4. The Kedro MCP server will be available with tools like `health_check`

### Manual Server Testing

Once `kedro-mcp` is installed, you can test the server directly using the MCP CLI:

```bash
# Start the server
kedro-mcp

# Or using uv (if installed)
uv run kedro-mcp
```

## Available Tools

Currently available MCP tools:

- **`health_check`**: Verify the MCP server is running and get server metadata

## Testing the Integration

1. Start your preferred AI assistant (Claude Desktop, VS Code with Claude Code Chat or Copilot)
2. Ask the assistant to use the `health_check` tool
3. You should receive a response indicating the server is running

Example conversation:
```
You: Can you check if the Kedro MCP server is working?
Assistant: I'll check the Kedro MCP server status for you.
[Uses health_check tool]
The Kedro MCP server is up and running! Version 0.0.1.dev0 is active.
```

## Troubleshooting

### Common Issues

1. **Server not starting**: Ensure Python 3.10+ is installed and `kedro-mcp` is installed in your virtual environment
2. **Tools not available in AI assistant**: Check the MCP server configuration in your AI assistant's settings

## Contributing

**Prerequisites**: Install [uv](https://docs.astral.sh/uv/) for dependency management.

1. Fork the repository

2. Create a feature branch: `git checkout -b feature-name`

3. Set up development environment:

   ```bash
   uv pip install -e . --group dev
   ```

4. Make your changes and add tests

5. Run linting and tests:
   ```bash
   ruff check .
   mypy src/
   ```

6. This project uses [pre-commit](https://pre-commit.com/) hooks to enforce code quality (linting and type checks) before every commit.
Make sure you have installed the Git hook:

  Run this once inside your local repo:
    ```bash
    pre-commit install
    ```
  This creates a .git/hooks/pre-commit script that will automatically run on git commit.

7. Submit a pull request

## License

This project is licensed under the Apache Software License 2.0. See LICENSE.txt for details.

## Support

- Report issues: [GitHub Issues](https://github.com/kedro-org/kedro-mcp/issues)
- MCP Specification: [Model Context Protocol](https://modelcontextprotocol.io/)
