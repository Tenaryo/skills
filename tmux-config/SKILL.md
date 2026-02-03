---
name: tmux-config
description: Comprehensive tmux terminal multiplexer configuration with official documentation lookup. Use when you need to configure tmux settings or create/modify .tmux.conf files, customize key bindings and status lines, troubleshoot tmux configuration issues, look up official tmux documentation or configuration patterns, or clone and access tmux wiki for reference. The skill ensures documentation is consulted before making configuration changes.
---

# Tmux Configuration Skill

## Overview

This skill provides systematic tmux configuration with mandatory documentation lookup. It includes tools to access the official tmux wiki and guidelines for finding configuration information from multiple sources.

## Configuration Workflow

Follow this sequence for all tmux configuration tasks:

### Step 1: Ensure Documentation is Available

Before any configuration, verify the tmux wiki is cloned locally:

```bash
python3 /root/.claude/skills/tmux-config/scripts/clone_wiki.py
```

This clones the wiki to the skill's `references/tmux-wiki` directory.

Update to get latest documentation:

```bash
python3 /root/.claude/skills/tmux-config/scripts/clone_wiki.py --update
```

### Step 2: Consult Official Documentation

**Always read official documentation before making configuration changes.**

Check the cloned wiki first:

```bash
# List available wiki files
python3 /root/.claude/skills/tmux-config/scripts/clone_wiki.py --list

# Get wiki path
python3 /root/.claude/skills/tmux-config/scripts/clone_wiki.py --get-path
```

Read relevant wiki pages using the `read` tool.

### Step 3: Check Additional Sources

If the wiki doesn't answer your question:

1. **Read man pages**: `man tmux` (read with Bash tool)
2. **Check tmux.conf syntax**: Look for configuration syntax and valid options
3. **Search official resources**: GitHub issues, mailing list archives

### Step 4: Search Online Resources (Fallback)

If official sources are insufficient, search online resources. See [document_lookup.md](document_lookup.md) for detailed search strategies and common configuration areas.

### Step 5: Implement Configuration

After consulting documentation:

1. **Create or edit `~/.tmux.conf`**
2. **Verify behavior**: Test the configured feature or key binding
3. **Document changes**: Add comments explaining the purpose of each configuration

#### Important: Maintain Consistent Code Style

When modifying `~/.tmux.conf`, follow the existing style conventions to maintain consistency:

**Section Organization:**
- Use separator lines: `# --------------------------------------------------------------------------`
- Section headers: `#  Section Title` (two-space indent after `#`)
- Group related configurations together
- Separate sections with blank lines

**Comment Style:**
- Section headers: `#  Section Name` (single line, no trailing comment)
- Separator lines: `# --------------------------------------------------------------------------` (78 dashes)
- Inline comments: End with brief description after the command
  ```bash
  bind -n M-h previous-window   # previous window with Alt+h
  ```
- Use `#` (single `#`) for all comments (not `##`)

**Configuration Format:**
- Global settings: `set -g option value` or `set-option -g option value`
- Key bindings: `bind [-n] [-r] key command` or `bind-key [-n] [-r] key command`
- Unbind keys: `unbind-key key` or `unbind key`
- Flags use `-g` (global), `-n` (no prefix), `-r` (repeatable)
- Align comments: Keep inline comments at consistent column (around column 50-60)

**Spacing and Formatting:**
- Blank lines between configuration groups
- Consistent indentation for related options
- Align similar options vertically when appropriate
- Plugin section at the end with `run '~/.tmux/plugins/...'`

**Examples from existing style:**
```bash
# --------------------------------------------------------------------------
#  Vim-style pane navigation (no prefix needed)
# --------------------------------------------------------------------------
bind -n C-h select-pane -L                  # left
bind -n C-j select-pane -D                  # down

# --------------------------------------------------------------------------
#  New custom key bindings
# --------------------------------------------------------------------------
bind -n M-h previous-window                 # previous window with Alt+h
bind -n M-l next-window                     # next window with Alt+l
```

**CRITICAL: Do NOT Test or Restart After Configuration**

After modifying `.tmux.conf`:
- ❌ **DO NOT** run `tmux start-server` or `tmux kill-server` for testing
- ❌ **DO NOT** restart the tmux server
- ❌ **DO NOT** run `tmux attach` or other commands that could disconnect users

**Why**: Testing with server commands may:
- Kill active tmux sessions and disconnect users
- Interrupt ongoing work in other tmux windows/panes
- Cause data loss in running applications
- Disrupt user workflows

**Safe Verification:**
- Syntax check only: `tmux -f ~/.tmux.conf start-server && echo "Config OK" && tmux kill-server`
- Note: This safe check should ONLY be used if no tmux sessions are active
- Best practice: Let users reload config themselves with `prefix + : source-file ~/.tmux.conf`

## Configuration Categories

### Basic Settings

Common basic configurations:
- Change prefix key (default: Ctrl-b)
- Enable mouse support
- Set default terminal and colors
- Configure window and pane indexing

Example search in wiki: Look for "prefix", "mouse", "terminal" keywords.

### Key Bindings

Customizing key bindings:
- Remap default keys to preferred combinations
- Create custom key sequences for common actions
- Change leader key behavior

Example search: Look for "bind-key", "unbind-key", "prefix" in documentation.

### Status Line

Configuring the status bar:
- Customize status line format and position
- Add dynamic information (time, hostname, load)
- Change colors and highlighting

Example search: Look for "status-line", "status-left", "status-right" in wiki.

### Appearance

Visual customization:
- Set color schemes
- Configure border styles
- Highlight active pane/window

Example search: Look for "colors", "pane-border", "window-status" in documentation.

## Documentation Lookup Strategy

Use the following approach when researching configuration options:

1. **Define the goal**: What specific behavior do you want to configure?
2. **Identify keywords**: Extract relevant terms (e.g., "split pane", "status line")
3. **Search wiki**: Grep the cloned wiki for these keywords
4. **Read man page section**: Use `man tmux | grep -A 10 keyword`
5. **Find examples**: Look for complete .tmux.conf examples in the wiki
6. **Verify syntax**: Ensure the configuration syntax matches tmux version

See [document_lookup.md](document_lookup.md) for comprehensive documentation lookup guidance.

## Testing Configuration

**WARNING: Do not test by running tmux commands after configuration changes.**

Testing should be done by the user to avoid disrupting active sessions:

1. **Backup existing config**: `cp ~/.tmux.conf ~/.tmux.conf.backup`
2. **Let user reload config**: Instruct user to press `prefix` + `:` then `source-file ~/.tmux.conf`
3. **User verification**: User should test the configured feature themselves
4. **Syntax-only check** (if needed, but be cautious):
   ```bash
   # ONLY if no active tmux sessions exist:
   tmux -f ~/.tmux.conf start-server && echo "Config OK" && tmux kill-server
   ```

**Why avoid testing:**
- `tmux start-server` or `kill-server` will disconnect all active users
- Interrupt ongoing work in other tmux windows/panes
- May cause data loss in running applications
- Disrupt user workflows and potentially lose unsaved work

## Common Configuration Patterns

### Enable Mouse Support

```bash
set -g mouse on
```

### Change Prefix to Ctrl-a

```bash
unbind C-b
set-option -g prefix C-a
bind C-a send-prefix
```

### Status Line with Time and Hostname

```bash
set -g status-right '%H:%M %Y-%m-%d'
set -g status-left '#H:#S'
```

## Resources

### scripts/

**clone_wiki.py** - Script to clone or update the tmux official wiki repository

Usage:
- `python3 scripts/clone_wiki.py` - Clone wiki (or show path if exists)
- `python3 scripts/clone_wiki.py --update` - Update wiki to latest
- `python3 scripts/clone_wiki.py --list` - List all wiki markdown files
- `python3 scripts/clone_wiki.py --get-path` - Get wiki path

### references/

**document_lookup.md** - Comprehensive guide for finding tmux configuration documentation

Contains:
- Official documentation lookup order
- Online resource links
- Search strategies and keywords
- Common configuration areas
- Step-by-step lookup workflow

**tmux-wiki/** - Complete tmux official wiki documentation

Contains official documentation files:
- Getting-Started.md - Comprehensive guide including configuration
- Recipes.md - Configuration file snippets and examples
- FAQ.md - Common questions and answers
- Advanced-Use.md - Advanced features
- Formats.md - Command and option formats
- And more...
