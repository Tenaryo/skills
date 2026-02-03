---
name: git-commit
description: Git workflow and commit conventions with semantic commit format. Use when working with Git operations, including configuration setup, committing changes with proper format, branch management, and following best practices for team collaboration. Essential for maintaining clean git history and ensuring consistent commit messages across projects.
---

# Git Commit Guide

## Overview

This skill provides standardized guidelines for Git operations, including user configuration, semantic commit format, workflow patterns, and best practices. Use this skill when creating commits, setting up Git for new projects, or establishing team standards.

## Git User Configuration

### Global Configuration

Set your identity globally (once per machine):

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Project-Specific Configuration

Override global settings for a specific project:

```bash
cd /path/to/project
git config user.name "Project Name"
git config user.email "project@example.com"
```

### Verify Configuration

Check current configuration:

```bash
git config --global user.name
git config --global user.email

# Or check all settings
git config --list
```

### Use Case for Project-Specific Config

Use project-specific config when:
- Working on behalf of organization account
- Different projects require different email domains
- Bot/automation commits need separate identity

## Semantic Commit Format

Always use `type(scope): message` format:

```
type(scope): subject

[optional body]

[optional footer]
```

### Types

| Type | Usage | Example |
|-------|---------|---------|
| `feat` | New feature | `feat(auth): add OAuth2 login support` |
| `fix` | Bug fix | `fix(api): resolve null pointer in user endpoint` |
| `docs` | Documentation only | `docs(readme): update installation instructions` |
| `style` | Code style/formatting | `style: remove trailing whitespace` |
| `refactor` | Code refactoring | `refactor(api): extract user service` |
| `perf` | Performance improvement | `perf(database): add query caching` |
| `test` | Add/update tests | `test(auth): add login validation tests` |
| `build` | Build system changes | `build: upgrade webpack to v5` |
| `ci` | CI/CD changes | `ci: add GitHub Actions workflow` |
| `chore` | Maintenance tasks | `chore: update dependencies` |
| `revert` | Revert previous commit | `revert: feat(api): add user endpoint` |

### Scopes

Scope limits the commit to a specific module or component:

```
Common scopes:
- api          - API layer
- ui/ux        - User interface
- auth         - Authentication
- database/db   - Database changes
- config       - Configuration
- docs         - Documentation
- tests/test    - Test files
- build        - Build system
- ci           - CI/CD

Example:
feat(api): add user registration endpoint
fix(ui): correct responsive layout
docs(readme): update setup instructions
```

**Rules for scope:**
- Keep it short (1-2 words)
- Use lowercase
- Separate multiple scopes with `/`: `feat(auth/api): add token refresh`
- Omit scope if change affects multiple areas

### Subject Line

```bash
# Good
feat(api): add user registration endpoint
fix(auth): resolve token expiration issue

# Bad
feat(api): Added user registration endpoint  (capitalized)
fix(auth): Token expiration issue           (missing imperative verb)
```

**Rules:**
- Imperative mood (add, fix, update, not added, fixed, updated)
- Lowercase after type
- No period at end
- Max 50 characters recommended

### Body and Footer

```bash
fix(api): resolve null pointer in user endpoint

Handle edge case where user object is not initialized
in cache miss scenario. Add null check before accessing
user properties.

Closes #123
Co-authored-by: Alice <alice@example.com>
```

**Body rules:**
- One blank line between subject and body
- Wrap at 72 characters
- Explain **what** and **why**, not **how**

**Footer uses:**
- `Closes #123` or `Fixes #456` for issue tracking
- `BREAKING CHANGE:` for breaking changes
- `Co-authored-by:` for collaboration

### Examples

```bash
# Simple feature
feat(auth): add password reset functionality

# Bug fix with body
fix(database): resolve connection timeout

Increase connection timeout from 30s to 60s to handle
slow network conditions in production environment.

# Documentation
docs(readme): update installation steps for macOS

Add Homebrew installation command and fix typo in
Python version requirement.

# Breaking change
feat(api): redesign user authentication model

BREAKING CHANGE: OAuth tokens now expire in 24 hours
instead of 7 days. Clients must implement token
refresh logic.
```

## Git Workflow

### Standard Workflow

```bash
# 1. Create branch from main/master
git checkout main && git pull
git checkout -b feature/add-login

# 2. Make changes and commit
git add .
git commit -m "feat(auth): add login form"

# 3. Push and create PR
git push -u origin feature/add-login
# Then create pull request on GitHub/GitLab

# 4. After merge, delete branch
git checkout main && git pull
git branch -d feature/add-login
```

### Commit Workflow

```bash
# Stage specific files
git add path/to/file.py

# Stage all changes
git add .

# Stage by pattern
git add *.py

# Commit with message
git commit -m "type(scope): message"

# Commit all tracked changes
git commit -am "type(scope): message"
```

### Amend Workflow

Modify most recent commit (before pushing):

```bash
# Add forgotten file
git add forgotten_file.py
git commit --amend

# Edit commit message
git commit --amend

# Both at once
git add forgotten_file.py
git commit --amend -m "fixed message"
```

**Warning:** Never amend commits that are already pushed.

## Branch Naming Conventions

### Standard Branch Names

| Type | Pattern | Example |
|-------|-----------|----------|
| Feature | `feature/` | `feature/user-authentication` |
| Bug fix | `fix/` | `fix/login-crash` |
| Hotfix | `hotfix/` | `hotfix/security-patch` |
| Release | `release/` | `release/v1.2.0` |
| Refactor | `refactor/` | `refactor/api-structure` |
| Chore | `chore/` | `chore/update-dependencies` |

### Branch Management

```bash
# List all branches
git branch -a

# Delete local branch
git branch -d feature/login

# Delete remote branch
git push origin --delete feature/login

# Rename branch
git branch -m old-name new-name

# Track remote branch
git checkout -b local-name origin/remote-name
```

## Common Commands

### Viewing History

```bash
# Show commits
git log

# Show commits one line
git log --oneline

# Show commit with diff
git log -p

# Show file history
git log -- path/to/file.py

# Show commit graph
git log --graph --oneline --all
```

### Checking Status

```bash
# Show working directory status
git status

# Show tracked files
git ls-files

# Show ignored files
git check-ignore -v
```

### Undoing Changes

```bash
# Unstage file
git restore --staged file.py

# Discard local changes
git restore file.py

# Unstage all
git reset

# Reset to commit (keep changes)
git reset HEAD~1

# Hard reset (discard changes)
git reset --hard HEAD~1
```

### Comparing Changes

```bash
# Show unstaged changes
git diff

# Show staged changes
git diff --staged

# Compare branches
git diff main..feature-login

# Compare commits
git diff abc123 def456
```

## Best Practices

### Commit Frequency

- **Commit often**: Small, focused commits are easier to review and revert
- **Commit complete units**: Don't commit broken code
- **Atomic changes**: One commit = one logical change
- **Test before commit**: Ensure code works

### Commit Message Quality

- **Be descriptive**: Others should understand the change without reading code
- **Be concise**: Subject lines should be <50 chars
- **Use active voice**: "Add feature" not "Feature was added"
- **Reference issues**: Link commits to tickets/PRs

### Branch Hygiene

- **Keep main/master clean**: Only merge tested PRs
- **Delete merged branches**: Remove feature branches after merge
- **Pull before branching**: Start from latest main/master
- **Rebase frequently**: Keep feature branches up to date with main

### Collaboration

- **Clear PR titles**: Use same format as commit messages
- **Describe PR changes**: Explain what and why
- **Request review**: Always have code reviewed
- **Resolve conflicts**: Be responsible for merge conflicts

## Resources

### references/

This skill includes reference materials for detailed commit type specifications and examples.

See [commit_types.md](references/commit_types.md) for comprehensive examples of commit types, scopes, and message patterns.

Use these references when unsure about appropriate commit type or need examples for specific scenarios.
