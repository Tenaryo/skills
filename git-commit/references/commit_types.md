# Git Commit Types Reference

## Overview

This document provides comprehensive examples and guidance for using semantic commit message format `type(scope): message`.

## Commit Types

### feat: New Feature

Use when adding a new feature or functionality.

**Examples:**
```bash
feat(auth): add OAuth2 authentication
feat(api): implement user registration endpoint
feat(ui): add dark mode toggle
feat(database): add user activity logging
feat(reporting): export to CSV functionality
```

**Characteristics:**
- Represents new capability
- Adds user-facing functionality
- May include breaking changes (document in footer)

### fix: Bug Fix

Use when fixing a bug or correcting an error.

**Examples:**
```bash
fix(api): resolve null pointer in user endpoint
fix(auth): correct token expiration logic
fix(ui): prevent button double-click
fix(database): resolve connection leak
fix(deploy): fix memory leak in worker process
```

**Characteristics:**
- Addresses a reported issue
- Fixes unexpected behavior
- Does not add new functionality

### docs: Documentation

Use when updating documentation.

**Examples:**
```bash
docs(readme): update installation instructions
docs(api): update authentication endpoint docs
docs(guide): add troubleshooting section
docs(schema): update database documentation
```

**Characteristics:**
- Only documentation changes
- No code changes (or trivial changes)
- Includes README, API docs, comments

### style: Code Style

Use when changing code style/formatting without functional changes.

**Examples:**
```bash
style: remove trailing whitespace
style(lint): fix code style violations
style(formatting): standardize indentation
style(naming): rename variables for consistency
```

**Characteristics:**
- No functional changes
- Formatting only
- Linter fixes

### refactor: Refactoring

Use when refactoring code without functional changes.

**Examples:**
```bash
refactor(api): extract user service
refactor(auth): simplify token validation
refactor(ui): component modularization
refactor(database): optimize query structure
```

**Characteristics:**
- Same behavior, better code
- Improves maintainability
- No external API changes

### perf: Performance

Use when improving performance.

**Examples:**
```bash
perf(api): add request caching
perf(database): add index to user table
perf(ui): optimize render loop
perf(worker): reduce memory usage
```

**Characteristics:**
- Improves speed or resource usage
- No functional changes
- Measurable performance gain

### test: Tests

Use when adding or updating tests.

**Examples:**
```bash
test(auth): add login validation tests
test(api): add integration tests
test(ui): add component unit tests
test(e2e): add end-to-end test suite
```

**Characteristics:**
- Only test file changes
- May include test infrastructure
- Test fixtures/mocks

### build: Build System

Use when changing build system or dependencies.

**Examples:**
```bash
build: upgrade webpack to v5
build(update): update Node.js to 18
build(maven): update plugin versions
build(npm): install new dependencies
```

**Characteristics:**
- Affects build process
- Dependency updates
- Configuration changes

### ci: CI/CD

Use when changing CI/CD configuration.

**Examples:**
```bash
ci(github): add automated testing workflow
ci(docker): add multi-stage build
ci(deploy): configure auto-deployment
ci(actions): add linting step
```

**Characteristics:**
- CI/CD pipeline changes
- GitHub Actions, GitLab CI, Jenkins
- Deployment configuration

### chore: Maintenance

Use when doing maintenance tasks.

**Examples:**
```bash
chore: update dependencies
chore(clean): remove unused files
chore(config): update environment variables
chore(script): add deployment script
```

**Characteristics:**
- Routine maintenance
- Not user-facing
- Configuration or tooling changes

### revert: Revert

Use when reverting a previous commit.

**Examples:**
```bash
revert: feat(api): add user endpoint

This reverts commit abc123.
Reason: Endpoint causes performance degradation.
```

**Characteristics:**
- Undoes a previous commit
- References original commit
- Explains reason

## Commit Scopes

### Common Scopes by Layer

#### API Layer
```
scope: api
```

**Examples:**
```bash
feat(api): add user registration endpoint
fix(api): resolve null pointer in response
docs(api): update API documentation
```

#### UI/UX Layer
```
scope: ui or ux
```

**Examples:**
```bash
feat(ui): add responsive navigation
fix(ux): improve button accessibility
style(ui): fix mobile layout
```

#### Authentication
```
scope: auth
```

**Examples:**
```bash
feat(auth): add OAuth2 login
fix(auth): correct token refresh logic
test(auth): add login validation tests
```

#### Database
```
scope: database or db
```

**Examples:**
```bash
feat(database): add user activity logging
perf(database): add index to email column
refactor(db): normalize user table structure
```

#### Configuration
```
scope: config
```

**Examples:**
```bash
chore(config): update default timeouts
feat(config): add environment variable support
docs(config): document new configuration options
```

#### Documentation
```
scope: docs
```

**Examples:**
```bash
docs(readme): update quick start guide
docs(api): update endpoint examples
docs(guide): add troubleshooting section
```

#### Tests
```
scope: tests or test
```

**Examples:**
```bash
test(api): add integration tests
test(auth): add login validation
test(e2e): add end-to-end test suite
```

#### Build System
```
scope: build
```

**Examples:**
```bash
build(webpack): upgrade to v5
build(maven): update plugin versions
build(docker): optimize image size
```

#### CI/CD
```
scope: ci
```

**Examples:**
```bash
ci(github): add automated testing
ci(docker): add build pipeline
ci(actions): add deployment workflow
```

### Module-Specific Scopes

For projects with specific modules, use module names:

```bash
feat(user): add profile picture upload
feat(order): add shopping cart
feat(payment): integrate Stripe API
fix(email): resolve attachment issues
refactor(notification): push notification service
```

### Multiple Scopes

When a commit affects multiple areas, separate with `/`:

```bash
feat(auth/api): add token refresh endpoint
fix(ui/database): correct user count display
docs(api/readme): update authentication examples
```

**When to use multiple scopes:**
- Changes touch multiple distinct areas
- Each scope represents a significant portion of the change
- Clear separation of concerns

**When to omit scope:**
- Changes affect many areas equally
- No single module dominates the change
- Broad infrastructure changes

## Full Message Examples

### Simple Feature
```bash
feat(auth): add password reset functionality
```

### Feature with Body
```bash
feat(api): add user registration endpoint

Implement POST /api/users endpoint with email validation
and password hashing. Returns 201 with user ID on success.

Closes #42
```

### Bug Fix with Explanation
```bash
fix(database): resolve connection timeout issue

Increase connection timeout from 30s to 60s to handle
slow network conditions in production environments.
Also add retry logic for transient failures.

Fixes #123
```

### Documentation Update
```bash
docs(readme): update installation steps for macOS

Add Homebrew installation command and correct typo
in Python version requirement (3.8+ not 3.6+).
```

### Refactoring
```bash
refactor(api): extract user service

Extract user-related business logic from controller
into separate UserService class for better testability
and reusability.
```

### Breaking Change
```bash
feat(api): redesign user authentication model

BREAKING CHANGE: OAuth tokens now expire in 24 hours
instead of 7 days. Clients must implement token
refresh logic to maintain sessions.

Closes #67
```

### Multi-Part Change
```bash
feat(auth/api): add token refresh endpoint

Implement refresh token generation and validation.
Also update client libraries to use new endpoint.

Partially addresses #45
```

## Common Mistakes

### Too Broad
```bash
# Bad
fix: fix bugs

# Good
fix(auth): resolve token expiration issue
fix(ui): prevent button double-click
```

### Missing Type
```bash
# Bad
Add login functionality

# Good
feat(auth): add OAuth2 login
```

### Wrong Type
```bash
# Bad (using feat for documentation)
feat: update README

# Good
docs(readme): update installation steps
```

### Capitalized Subject
```bash
# Bad
feat(Api): Add User Endpoint

# Good
feat(api): add user endpoint
```

### Period at End
```bash
# Bad
feat(auth): add login form.

# Good
feat(auth): add login form
```

### Too Long Subject
```bash
# Bad (over 50 chars)
feat(auth): implement complete user authentication system with OAuth2 support and token management

# Good (split into multiple commits)
feat(auth): add OAuth2 login
feat(auth): add token management
```

## Footer Examples

### Issue References
```bash
# GitHub/GitLab style
Closes #123
Fixes #456
Resolves #789

# Jira style
PROJ-123
```

### Breaking Changes
```bash
feat(api): redesign authentication model

BREAKING CHANGE: Removed legacy API endpoints.
Clients must migrate to v2 API.

BREAKING CHANGE: User email field is now required.
Existing users without email will be prompted to provide it.
```

### Co-authored-by
```bash
feat(auth): add 2FA support

Implemented by Alice and Bob.

Co-authored-by: Alice <alice@example.com>
Co-authored-by: Bob <bob@example.com>
```

### Multiple Footers
```bash
feat(api): add user deletion endpoint

Closes #123
BREAKING CHANGE: Soft delete replaces hard delete.
Users can be restored within 30 days.
```

## Language Tips

### Active Voice
```bash
# Bad
Feature was added to handle authentication.
Bug was fixed in token validation.

# Good
feat: add authentication support
fix: resolve token validation issue
```

### Imperative Mood
```bash
# Bad
Added login form.
Updating documentation.
Fixed memory leak.

# Good
feat: add login form
docs: update documentation
fix: resolve memory leak
```

### Concise Description
```bash
# Bad
fix(api): fix the issue where the API returns a null pointer when the user object is not initialized in the cache miss scenario

# Good
fix(api): resolve null pointer in user endpoint
```

### Explain What and Why
```bash
# Bad (only describes what)
fix: Add timeout parameter

# Good (explains why)
fix: add connection timeout to prevent hanging
requests on slow networks.
```

## Summary

Use this reference when:
- Uncertain about commit type for a change
- Need examples of proper commit messages
- Writing breaking changes or issue references
- Troubleshooting common commit message errors

Remember:
- Format: `type(scope): subject`
- Subject: Imperative, <50 chars, no period
- Body: Explain what and why, not how
- Footer: References, breaking changes, co-authors
