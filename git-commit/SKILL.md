---
name: git-commit
description: Git workflow and commit conventions with semantic commit format. Use when working with Git operations, including configuration setup, committing changes with proper format, branch management, and following best practices for team collaboration. Essential for maintaining clean git history and ensuring consistent commit messages across projects.
---

# Git Commit Guide

## Overview

This skill provides standardized guidelines for Git operations, including user configuration, semantic commit format, workflow patterns, and best practices. Use this skill when creating commits, setting up Git for new projects, or establishing team standards.

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

### Examples

```bash
# Simple feature for issue 1532 (seen from the branch name if exists)
feat(auth): #1532 add password reset functionality

# Bug fix with body for issue 1787 (seen from the branch name if exists)
fix(database): # 1787 resolve connection timeout

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
