#!/usr/bin/env python3
"""
Simple hashing helper for beginner-friendly malware analysis workflows.

Usage:
    python analysis/scripts/hash_report.py <file_path>
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


CHUNK_SIZE = 8192


def compute_hash(path: Path, algorithm: str) -> str:
    hasher = hashlib.new(algorithm)
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(CHUNK_SIZE)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Print basic hash and metadata information for a file."
    )
    parser.add_argument("file_path", help="Path to the target file")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    target = Path(args.file_path)

    if not target.exists():
        parser.error(f"file not found: {target}")

    if not target.is_file():
        parser.error(f"path is not a file: {target}")

    size = target.stat().st_size
    print("=== Hash Report ===")
    print(f"File    : {target.resolve()}")
    print(f"Size    : {size} bytes")
    print(f"MD5     : {compute_hash(target, 'md5')}")
    print(f"SHA1    : {compute_hash(target, 'sha1')}")
    print(f"SHA256  : {compute_hash(target, 'sha256')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
