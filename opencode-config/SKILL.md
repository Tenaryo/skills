---
name: opencode-config
description: OpenCode configuration and setup with official documentation lookup. Use when configuring OpenCode, understanding OpenCode settings, creating or modifying OpenCode config files, troubleshooting OpenCode configuration issues, looking up official OpenCode documentation, or setting up OpenCode for different usage modes (TUI, CLI, Web, IDE, GitHub, GitLab). The skill ensures official documentation is consulted before making configuration changes.
---

# OpenCode Configuration

## Overview

This skill provides systematic OpenCode configuration with mandatory documentation lookup. It includes tools to access official OpenCode documentation and guidance for finding configuration information from official sources.

## Ensure Documentation is Available

Before any configuration, verify OpenCode documentation is available locally:

```bash
python3 /root/.claude/skills/opencode-config/scripts/fetch_docs.py
```

This fetches documentation to skill's `references/opencode-docs` directory.

Update to get latest documentation:

```bash
python3 /root/.claude/skills/opencode-config/scripts/fetch_docs.py --update
```

## Consult Official Documentation

Always read official documentation before making configuration changes.

Check local documentation:

```bash
# List available documentation pages
python3 /root/.claude/skills/opencode-config/scripts/fetch_docs.py --list

# Get docs path
python3 /root/.claude/skills/opencode-config/scripts/fetch_docs.py --get-path
```

Read relevant documentation pages using `read` tool.

## Configuration File Location

OpenCode uses a TOML configuration file. The default location depends on OS:

- **Linux/macOS**: `~/.config/opencode/config.toml`
- **Windows**: `%APPDATA%\opencode\config.toml`

Specify a custom config file with the `--config` flag.

## Configuration Reference

### Model Configuration

```toml
[model]
name = "claude-3-5-sonnet"

[model.parameters]
temperature = 0.7
max_tokens = 4096
```

See `config/index.html` in local documentation for complete model configuration options.

### Provider Configuration

```toml
[provider]
name = "anthropic"

[provider.api_key]
value = "your-api-key-here"
```

Alternatively, use environment variables instead of hardcoding API keys:

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
export OPENAI_API_KEY="sk-..."
```

See `providers/index.html` for all provider options.

### Network Configuration

```toml
[network]
timeout = 30
retry_attempts = 3
```

See `network/index.html` for network settings.

## Usage Modes

### TUI (Terminal Interface)

```toml
[tui]
theme = "opencode"
font_size = 14
key_bindings = "vim"
```

See `tui/index.html` for TUI-specific settings.

### CLI

Configure CLI behavior with default commands and aliases. See `cli/index.html`.

### Web

Web interface settings for browser-based usage. See `web/index.html`.

### IDE Integration

```toml
[ide]
enabled = true
server_port = 8080
auto_start = true
```

See `ide/index.html` for IDE integration.

## Tools Configuration

Configure enabled tools and their settings:

```toml
[tools]
enabled = ["edit", "write", "read", "bash", "grep", "glob"]

[tools.edit]
auto_save = true

[tools.bash]
timeout = 30
working_directory = "/root"
```

See `tools/index.html` for complete tool reference.

## Rules Configuration

Customize AI behavior with rules:

```toml
[[rules]]
name = "no-external-services"
description = "Do not use external services without explicit permission"
enabled = true
```

See `rules/index.html` for rule configuration.

## Skills Configuration

Configure agent skills:

```toml
[skills]
enabled = ["git-master", "playwright", "frontend-ui-ux"]
skills_directory = "~/.claude/skills"
```

See `skills/index.html` for skill configuration.

## Common Issues

### API Key Not Found

Check environment variables: `echo $ANTHROPIC_API_KEY`

Verify config file syntax in `config/index.html`.

### Network Timeout

Increase timeout: `[network] timeout = 60`

Verify API endpoint accessibility in `network/index.html`.

### Model Not Available

Verify model name spelling in `models/index.html`.

Check if provider supports the model.

For comprehensive troubleshooting, see `troubleshooting/index.html`.

## Documentation Lookup

Use this approach when researching configuration options:

1. Define the goal: What specific behavior do you want to configure?
2. Identify keywords: Extract relevant terms (e.g., "api key", "model", "theme")
3. Search local docs: Grep the downloaded documentation for these keywords
4. Check relevant sections: Focus on specific documentation pages
5. Find examples: Look for complete configuration examples in docs
6. Verify syntax: Ensure configuration matches OpenCode version

## Testing Configuration

After making changes:

1. Validate syntax: OpenCode will report syntax errors on startup
2. Test with simple command: Run a basic OpenCode command to verify connection
3. Check logs: Review OpenCode logs for errors or warnings
4. Test specific feature: Verify that configured feature works as expected

## Resources

### scripts/

**fetch_docs.py** - Script to fetch or update OpenCode documentation

Usage:
- `python3 scripts/fetch_docs.py` - Fetch docs (or show path if exists)
- `python3 scripts/fetch_docs.py --update` - Update docs to latest
- `python3 scripts/fetch_docs.py --list` - List all documentation HTML files
- `python3 scripts/fetch_docs.py --get-path` - Get docs path
- `python3 scripts/fetch_docs.py --force` - Force refetch if directory exists

### references/

**opencode-docs/** - Complete OpenCode official documentation

Contains official documentation files:
- `index.html` - Main introduction
- `config/index.html` - Configuration reference
- `providers/index.html` - Provider configuration
- `models/index.html` - Model settings
- `tools/index.html` - Tools configuration
- `rules/index.html` - Rules configuration
- `skills/index.html` - Agent skills
- `troubleshooting/index.html` - Troubleshooting guide
- And many more...
