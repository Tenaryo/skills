# Claude Skills Repository

This repository contains custom Claude AI skills for the OhMyOpenCode system.

## Available Skills

### tmux-config
Comprehensive tmux terminal multiplexer configuration with official documentation lookup. Use when you need to configure tmux settings or create/modify `.tmux.conf` files, customize key bindings and status lines, troubleshoot tmux configuration issues, look up official tmux documentation or configuration patterns, or clone and access tmux wiki for reference.

**Contents:**
- `SKILL.md` - Main skill documentation
- `scripts/clone_wiki.py` - Script to clone/update tmux official wiki
- `references/document_lookup.md` - Documentation lookup guide

**Note:** The tmux wiki documentation can be downloaded by running:
```bash
python3 scripts/clone_wiki.py
```

### skill-creator
Guide for creating effective skills. This skill should be used when you want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.

**Contents:**
- `SKILL.md` - Main skill documentation
- `scripts/init_skill.py` - Initialize a new skill
- `scripts/quick_validate.py` - Quick validation tool
- `references/workflows.md` - Workflow patterns
- `references/output-patterns.md` - Output formatting patterns

## Usage

These skills are loaded by Claude automatically when available. Each skill provides specialized knowledge and workflows for specific tasks.

## Structure

```
.
├── .gitignore              # Git ignore patterns
├── README.md               # This file
├── tmux-config/           # tmux configuration skill
│   ├── SKILL.md
│   ├── scripts/
│   └── references/
├── git-commit/             # Git workflow and commit conventions skill
│   ├── SKILL.md
│   └── references/
└── skill-creator/         # Skill creation guide
    ├── SKILL.md
    ├── scripts/
    └── references/
```

## Contributing

To add a new skill:

1. Use `skill-creator` skill as a template
2. Create your skill directory following to same structure
3. Add a `SKILL.md` file with comprehensive documentation
4. Include necessary scripts and references

## License

See individual skill documentation for licensing information.

## Support

For issues or questions about specific skills, please refer to their respective `SKILL.md` files.
