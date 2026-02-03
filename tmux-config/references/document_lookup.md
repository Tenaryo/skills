# Document Lookup Guide for tmux Configuration

When configuring tmux, follow this lookup order:

## 1. Official Documentation (Primary Source)

**Location**: skill's references/tmux-wiki/ directory (managed by scripts/clone_wiki.py)

Check the wiki first for:
- Configuration options (`~/.tmux.conf`)
- Key bindings and commands
- Common configuration patterns
- FAQ and troubleshooting

Key files to check:
- `Index.md` - Main index page
- Configuration-related pages (look for keywords: "config", "conf", "settings")
- FAQ pages for common issues

## 2. Online Official Resources

If the wiki doesn't have the answer, search these official sources:

- **tmux man pages**: Run `man tmux` for comprehensive documentation
- **tmux GitHub issues**: https://github.com/tmux/tmux/issues - Search existing issues
- **tmux mailing list**: Check archives for configuration discussions

## 3. Community Resources (Fallback)

When official sources don't help, search these community resources:

**Documentation sites:**
- tmux cheatsheets and configuration guides
- Blog posts about tmux configuration
- Configuration sharing sites (dotfiles repositories)

**Search queries to use:**
- "tmux [feature] configuration"
- "tmux.conf [specific setting]"
- "tmux [keybinding] change"

**Keywords to search for:**
- `tmux.conf examples`
- `tmux configuration tutorial`
- `tmux keybinding customization`
- `tmux status line configuration`
- `tmux pane management`

## 4. Common Configuration Areas

When looking up documentation, focus on these common configuration areas:

### Basic Configuration
- Prefix key (default: Ctrl-b)
- Enable mouse support
- Set default shell
- Terminal type and colors

### Window and Pane Management
- Window creation and switching
- Pane splitting and navigation
- Pane resizing

### Status Line
- Customizing status line format
- Adding information (time, battery, load average)
- Colors and formatting

### Key Bindings
- Remapping default keys
- Creating custom key combinations
- Leader key behavior

### Appearance
- Color schemes
- Border styles
- Active pane highlighting

## Workflow for Config Lookup

1. **Identify the area**: What do you want to configure?
2. **Search the wiki first**: Use the `read` tool on wiki files in references/tmux-wiki/
3. **Check man pages**: Run `man tmux` for detailed command documentation
4. **Search online**: Use targeted queries with "tmux" + specific keywords
5. **Save to .tmux.conf**: Add to your configuration file
