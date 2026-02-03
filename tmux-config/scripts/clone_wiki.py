#!/usr/bin/env python3
"""
Clone or update the tmux official wiki repository.

This script manages the tmux.wiki repository, ensuring that the latest
official documentation is available locally for configuration reference.
"""

import os
import subprocess
import sys
import argparse
from pathlib import Path

TMUX_WIKI_URL = "https://github.com/tmux/tmux.wiki.git"

SCRIPT_DIR = Path(__file__).parent.parent
DEFAULT_CLONE_PATH = SCRIPT_DIR / "references" / "tmux-wiki"


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


def clone_wiki(clone_path=None, force=False):
    """
    Clone the tmux wiki repository.

    Args:
        clone_path: Path where to clone the wiki (default: ~/.tmux-wiki)
        force: If True, clone even if directory exists

    Returns:
        Path to the wiki repository or None on failure
    """
    if clone_path is None:
        clone_path = DEFAULT_CLONE_PATH

    clone_path = Path(clone_path).expanduser()

    if clone_path.exists():
        if clone_path.is_dir():
            if force:
                print(f"Removing existing directory: {clone_path}")
                run_command(f"rm -rf {clone_path}")
                if clone_path.exists():
                    print("Failed to remove existing directory")
                return None

    print(f"Cloning tmux wiki to: {clone_path}")

    clone_path.parent.mkdir(parents=True, exist_ok=True)

    if run_command(f"git clone {TMUX_WIKI_URL} {clone_path}") is not None:
        print(f"✅ Successfully cloned tmux wiki")
        print(f"   Location: {clone_path}")
        return clone_path
    else:
        print("❌ Failed to clone tmux wiki")
        return None


def update_wiki(clone_path=None):
    """
    Update the tmux wiki repository.

    Args:
        clone_path: Path to the wiki repository (default: ~/.tmux-wiki)

    Returns:
        True on success, False on failure
    """
    if clone_path is None:
        clone_path = DEFAULT_CLONE_PATH

    clone_path = Path(clone_path).expanduser()

    if not clone_path.exists():
        print(f"Wiki not found at: {clone_path}")
        print("Use --clone to clone the wiki first")
        return False

    print(f"Updating tmux wiki at: {clone_path}")

    if run_command("git fetch origin", cwd=clone_path) is not None:
        if run_command("git pull origin main", cwd=clone_path) is not None:
            print("✅ Successfully updated tmux wiki")
            return True

    print("❌ Failed to update tmux wiki")
    return False


def get_wiki_path(clone_path=None):
    """
    Get the path to the wiki repository.

    Args:
        clone_path: Path to the wiki repository (default: ~/.tmux-wiki)

    Returns:
        Path to the wiki or None if not found
    """
    if clone_path is None:
        clone_path = DEFAULT_CLONE_PATH

    clone_path = Path(clone_path).expanduser()

    if clone_path.exists() and clone_path.is_dir():
        return clone_path
    return None


def list_wiki_files(clone_path=None):
    """
    List all markdown files in the wiki.

    Args:
        clone_path: Path to the wiki repository (default: ~/.tmux-wiki)

    Returns:
        List of markdown file paths
    """
    wiki_path = get_wiki_path(clone_path)
    if not wiki_path:
        print("Wiki not found. Clone or update it first.")
        return []

    md_files = list(wiki_path.glob("*.md"))
    return sorted(md_files)


def main():
    parser = argparse.ArgumentParser(
        description="Clone or update the tmux official wiki"
    )
    parser.add_argument("--clone", action="store_true", help="Clone the tmux wiki")
    parser.add_argument("--update", action="store_true", help="Update the tmux wiki")
    parser.add_argument(
        "--force", action="store_true", help="Force reclone if directory exists"
    )
    parser.add_argument(
        "--path", type=str, default=None, help="Custom path for wiki clone"
    )
    parser.add_argument("--list", action="store_true", help="List wiki markdown files")
    parser.add_argument("--get-path", action="store_true", help="Get the wiki path")

    args = parser.parse_args()

    if not any([args.clone, args.update, args.list, args.get_path]):
        wiki_path = get_wiki_path(args.path)
        if wiki_path:
            print(f"Wiki already exists at: {wiki_path}")
        else:
            clone_wiki(args.path)
        return

    if args.clone:
        clone_wiki(args.path, args.force)

    if args.update:
        update_wiki(args.path)

    if args.list:
        files = list_wiki_files(args.path)
        if files:
            print("\nWiki markdown files:")
            for f in files:
                print(f"  - {f.name}")

    if args.get_path:
        wiki_path = get_wiki_path(args.path)
        if wiki_path:
            print(wiki_path)
        else:
            sys.exit(1)


if __name__ == "__main__":
    main()
