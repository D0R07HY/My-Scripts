#!/usr/bin/env python3
"""
Extract printable strings from a file for beginner-friendly static analysis.

Usage:
    python analysis/scripts/basic_strings.py <file_path>
    python analysis/scripts/basic_strings.py <file_path> --min-length 6
    python analysis/scripts/basic_strings.py <file_path> --output strings.txt
"""

from __future__ import annotations

import argparse
from pathlib import Path


PRINTABLE_ASCII_MIN = 32
PRINTABLE_ASCII_MAX = 126


def is_printable(byte_value: int) -> bool:
    return PRINTABLE_ASCII_MIN <= byte_value <= PRINTABLE_ASCII_MAX


def extract_strings(data: bytes, min_length: int) -> list[str]:
    results: list[str] = []
    current: list[str] = []

    for byte_value in data:
        if is_printable(byte_value):
            current.append(chr(byte_value))
            continue

        if len(current) >= min_length:
            results.append("".join(current))
        current = []

    if len(current) >= min_length:
        results.append("".join(current))

    return results


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Extract printable ASCII strings from a file."
    )
    parser.add_argument("file_path", help="Path to the target file")
    parser.add_argument(
        "--min-length",
        type=int,
        default=4,
        help="Minimum string length to keep (default: 4)",
    )
    parser.add_argument(
        "--output",
        help="Optional output text file path",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.min_length < 1:
        parser.error("--min-length must be at least 1")

    target = Path(args.file_path)
    if not target.exists():
        parser.error(f"file not found: {target}")
    if not target.is_file():
        parser.error(f"path is not a file: {target}")

    data = target.read_bytes()
    strings_found = extract_strings(data, args.min_length)

    if args.output:
        output_path = Path(args.output)
        output_path.write_text("\n".join(strings_found), encoding="utf-8")
        print(f"Saved {len(strings_found)} strings to {output_path.resolve()}")
    else:
        for line in strings_found:
            print(line)
        print(f"\nTotal strings found: {len(strings_found)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
