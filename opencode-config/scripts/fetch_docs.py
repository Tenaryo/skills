#!/usr/bin/env python3
"""
Fetch or update OpenCode official documentation.

This script manages OpenCode documentation from https://opencode.ai/docs/,
ensuring that the latest official documentation is available locally for reference.
"""

import os
import subprocess
import sys
import argparse
from pathlib import Path

OPENCODE_DOCS_URL = "https://opencode.ai/docs/"

SCRIPT_DIR = Path(__file__).parent.parent
DEFAULT_DOCS_PATH = SCRIPT_DIR / "references" / "opencode-docs"


def run_command(cmd, cwd=None):
    """Execute a shell command and return its output."""
    try:
        result = subprocess.run(
            cmd, shell=True, check=True, cwd=cwd, capture_output=True, text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {cmd}")
        print(f"Error: {e.stderr}")
        return None


def fetch_docs(docs_path=None, force=False):
    """
    Fetch OpenCode documentation.

    Args:
        docs_path: Path where to save docs (default: references/opencode-docs)
        force: If True, fetch even if directory exists

    Returns:
        Path to the docs directory or None on failure
    """
    if docs_path is None:
        docs_path = DEFAULT_DOCS_PATH

    docs_path = Path(docs_path).expanduser()

    if docs_path.exists():
        if docs_path.is_dir():
            if force:
                print(f"Removing existing directory: {docs_path}")
                run_command(f"rm -rf {docs_path}")
                if docs_path.exists():
                    print("Failed to remove existing directory")
                    return None
            else:
                print(f"Documentation already exists at: {docs_path}")
                print("Use --force to refetch")
                return docs_path

    print(f"Fetching OpenCode documentation to: {docs_path}")

    docs_path.parent.mkdir(parents=True, exist_ok=True)

    # Use wget to mirror the documentation site
    # -r: recursive
    # -np: don't ascend to parent directory
    # -nH: don't create host directories
    # --cut-dirs=1: remove /docs/ from path
    # -k: convert links for local viewing
    # -p: download page requisites (images, css, etc)
    # -E: save HTML files with .html extension
    # -A "*.html,*.css,*.js,*.svg,*.png,*.jpg,*.jpeg,*.webp": accept these file types
    wget_cmd = (
        f"wget -r -np -nH --cut-dirs=1 -k -p -E "
        f"-A '*.html,*.css,*.js,*.svg,*.png,*.jpg,*.jpeg,*.webp' "
        f"{OPENCODE_DOCS_URL} -P {docs_path.parent}"
    )

    if run_command(wget_cmd) is not None:
        print(f"Successfully fetched OpenCode documentation")
        print(f"   Location: {docs_path}")

        docs_dir = docs_path.parent / "docs"
        if docs_dir.exists() and not docs_path.exists():
            docs_dir.rename(docs_path)

        return docs_path
    else:
        print("Failed to fetch OpenCode documentation")
        return None


def update_docs(docs_path=None):
    """
    Update OpenCode documentation.

    Args:
        docs_path: Path to the docs directory (default: references/opencode-docs)

    Returns:
        True on success, False on failure
    """
    if docs_path is None:
        docs_path = DEFAULT_DOCS_PATH

    docs_path = Path(docs_path).expanduser()

    if not docs_path.exists():
        print(f"Documentation not found at: {docs_path}")
        print("Use --fetch to fetch documentation first")
        return False

    print(f"Updating OpenCode documentation at: {docs_path}")

    if run_command(f"rm -rf {docs_path}") is not None:
        return fetch_docs(docs_path, force=False) is not None

    print("Failed to update OpenCode documentation")
    return False


def get_docs_path(docs_path=None):
    """
    Get the path to the documentation directory.

    Args:
        docs_path: Path to the docs directory (default: references/opencode-docs)

    Returns:
        Path to the docs or None if not found
    """
    if docs_path is None:
        docs_path = DEFAULT_DOCS_PATH

    docs_path = Path(docs_path).expanduser()

    if docs_path.exists() and docs_path.is_dir():
        return docs_path
    return None


def list_docs_files(docs_path=None):
    """
    List all HTML files in the documentation.

    Args:
        docs_path: Path to the docs directory (default: references/opencode-docs)

    Returns:
        List of HTML file paths
    """
    docs_path = get_docs_path(docs_path)
    if not docs_path:
        print("Documentation not found. Fetch it first.")
        return []

    html_files = list(docs_path.rglob("*.html"))
    return sorted(html_files)


def main():
    parser = argparse.ArgumentParser(
        description="Fetch or update OpenCode official documentation"
    )
    parser.add_argument("--fetch", action="store_true", help="Fetch the documentation")
    parser.add_argument(
        "--update", action="store_true", help="Update the documentation"
    )
    parser.add_argument(
        "--force", action="store_true", help="Force refetch if directory exists"
    )
    parser.add_argument("--path", type=str, default=None, help="Custom path for docs")
    parser.add_argument(
        "--list", action="store_true", help="List documentation HTML files"
    )
    parser.add_argument("--get-path", action="store_true", help="Get the docs path")

    args = parser.parse_args()

    if not any([args.fetch, args.update, args.list, args.get_path]):
        docs_path = get_docs_path(args.path)
        if docs_path:
            print(f"Documentation already exists at: {docs_path}")
        else:
            fetch_docs(args.path)
        return

    if args.fetch:
        fetch_docs(args.path, args.force)

    if args.update:
        update_docs(args.path)

    if args.list:
        files = list_docs_files(args.path)
        if files:
            print("\nDocumentation HTML files:")
            for f in files:
                rel_path = f.relative_to(get_docs_path(args.path) or DEFAULT_DOCS_PATH)
                print(f"  - {rel_path}")

    if args.get_path:
        docs_path = get_docs_path(args.path)
        if docs_path:
            print(docs_path)
        else:
            sys.exit(1)


if __name__ == "__main__":
    main()
