---
name: config-workflow
description: Standard workflow for all configuration tasks. Use before modifying ANY config files (nvim, tmux, git, shell, applications, plugins, etc.). Ensures proper documentation lookup before making changes.
---

# Configuration Workflow Skill

## Core Principle

**Never configure without documentation.** Always verify understanding before editing config files.

## Workflow

### Step 1: Check Existing Skills

First, check if a specific skill exists for the tool:
- Run: `skill` tool or check `/home/tylertan/.claude/skills/`
- If skill exists: Follow its instructions (e.g., `tmux-config` for tmux)
- If no skill: Continue to Step 2

### Step 2: Consult Official Documentation

Always read official docs first:
- **Man pages**: `man <tool>` (e.g., `man nvim`)
- **Official docs**: Search tool's official website or GitHub README
- **Help commands**: `<tool> --help` or `:<help>` in interactive tools

### Step 3: Search Online (Fallback)

If official docs are unclear:
- Search: "[tool] configure [feature] official documentation"
- Prefer: Official GitHub issues, Stack Overflow with official answers
- Verify: Check that answers are recent and match tool version

## Common Config Locations

| Tool | Config Location |
|------|-----------------|
| nvim | `~/.config/nvim/` |
| tmux | `~/.tmux.conf` |
| git | `~/.gitconfig` |
| zsh | `~/.zshrc` |


## Prohibition

**DO NOT**:
- Edit config files without understanding what they do
- Copy-paste config snippets from random sources
- Assume config syntax without verification
