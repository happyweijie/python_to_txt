"""Copy Python files under a directory to .txt files in a new directory.

The conversion preserves file contents and folder structure. Common
generated/cache directories are skipped by default.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


IGNORED_DIRS = {
    "__pycache__",
    ".git",
    ".hg",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".tox",
    ".venv",
    "venv",
    "env",
    "build",
    "dist",
}


def iter_python_files(root: Path):
    for path in root.rglob("*.py"):
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        if path.is_file():
            yield path


def convert(
    source_root: Path,
    output_root: Path,
    *,
    dry_run: bool = False,
    overwrite: bool = False,
) -> int:
    count = 0

    for source in iter_python_files(source_root):
        relative_path = source.relative_to(source_root)
        target = output_root / relative_path.with_suffix(".txt")

        if target.exists() and not overwrite:
            raise FileExistsError(
                f"Target already exists: {target}. Use --overwrite to replace it."
            )

        print(f"{source} -> {target}")
        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
        count += 1

    return count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy all .py files in a directory tree to .txt files."
    )
    parser.add_argument("source_directory", type=Path, help="Directory to convert.")
    parser.add_argument(
        "output_directory",
        type=Path,
        nargs="?",
        help=(
            "New directory where converted files will be written. Defaults to a "
            "sibling folder named SOURCE_txt."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show the files that would be renamed without changing anything.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace existing .txt targets in the output directory.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source_root = args.source_directory.resolve()

    if not source_root.is_dir():
        raise NotADirectoryError(f"Directory does not exist: {source_root}")

    output_root = (
        args.output_directory.resolve()
        if args.output_directory
        else source_root.parent / f"{source_root.name}_txt"
    )

    if output_root == source_root or source_root in output_root.parents:
        raise ValueError("Output directory must be separate from the source directory.")

    count = convert(
        source_root,
        output_root,
        dry_run=args.dry_run,
        overwrite=args.overwrite,
    )
    action = "Would convert" if args.dry_run else "Converted"
    print(f"{action} {count} file(s).")


if __name__ == "__main__":
    main()
