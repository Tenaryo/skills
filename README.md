# Opencode Skills

Tyler Tan's personal collection of [opencode](https://opencode.ai) skills, designed for C++ development workflows.

## About

These skills are primarily tailored for **C++ development**, leveraging modern C++ features (C++17/20/23/26) with a strong emphasis on performance engineering. The three core workflow skills (`feat-workflow`, `fix-workflow`, `review-workflow`) follow an architect-engineer collaboration model, where the user acts as the architect and the AI as a senior engineer who must get design and implementation decisions approved step by step.

> **Other languages**: These skills can be adapted for other languages. To do so, modify the skill descriptions and coding conventions (e.g., replace C++ toolchain references like `clang-format` with your language's equivalents, adjust the "modern C++ features" guidance, etc.).

## Included Skills

| Skill | Description |
|-------|-------------|
| **feat-workflow** | Test-driven feature development with isolated git worktree and collaborative design process |
| **fix-workflow** | Bug fixing with reproduction testing, root cause analysis, and architect-collaborative fix approval |
| **review-workflow** | Systematic C++ code review and refactoring across multiple dimensions (performance, modern style, safety, etc.) |
| **explain-code** | Step-by-step code explanation from architecture to implementation details (Chinese) |
| **skill-creator** | Guide for creating new opencode skills |

## Key Design Principles

- **TDD-first**: Write tests before implementation (`feat-workflow`, `fix-workflow`)
- **Incremental approval**: Every design decision and code change must be approved by the architect one at a time
- **Git worktree isolation**: All work happens in isolated worktrees with clean rebase-based merging
- **Layered design review**: Design decisions are reviewed top-down from architecture (L1) to implementation details (L5), with concrete code reviewed separately
- **Context-rich communication**: Code snippets, call chains, and module structures are presented in the main output, with only short approval questions in the `question` tool

## Usage

Place this repository (or symlink it) in your opencode skills directory. See [opencode documentation](https://opencode.ai) for details on skill installation.

## License

This project is licensed under the [MIT License](LICENSE).
