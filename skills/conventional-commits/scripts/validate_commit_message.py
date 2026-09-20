#!/usr/bin/env python3
"""Validate the portable structure of a Conventional Commits 1.0.0 message."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


HEADER_PATTERN = re.compile(
    r"^(?P<type>[A-Za-z][A-Za-z0-9-]*)"
    r"(?:\((?P<scope>[^()\r\n]+)\))?"
    r"(?P<breaking>!)?: (?P<description>\S.*)$"
)
FOOTER_PATTERN = re.compile(
    r"^(?:BREAKING CHANGE|BREAKING-CHANGE|[A-Za-z0-9-]+)(?:: | #)\S.*$"
)


def read_message(args: argparse.Namespace) -> str:
    if args.message is not None:
        return args.message
    if args.file is not None:
        return args.file.read_text(encoding="utf-8")
    return sys.stdin.read()


def validate(message: str) -> list[str]:
    errors: list[str] = []
    normalized = message.replace("\r\n", "\n").rstrip("\n")
    if not normalized:
        return ["message is empty"]

    lines = normalized.split("\n")
    header = lines[0]
    match = HEADER_PATTERN.fullmatch(header)
    if not match:
        errors.append(
            "header must match <type>[optional scope][optional !]: <description>"
        )
        return errors

    if match.group("type") != match.group("type").lower():
        errors.append("type should be lowercase for ecosystem compatibility")

    if len(lines) > 1 and lines[1] != "":
        errors.append("body or footers must begin after a blank line")

    for index, line in enumerate(lines[2:], start=3):
        if line.startswith(("BREAKING CHANGE", "BREAKING-CHANGE")) and not FOOTER_PATTERN.fullmatch(line):
            errors.append(f"line {index} has an invalid breaking-change footer")

    return errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--message", help="commit message to validate")
    source.add_argument("--file", type=Path, help="read the commit message from a file")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    errors = validate(read_message(args))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("VALID: Conventional Commits 1.0.0 structure")
    return 0


if __name__ == "__main__":
    sys.exit(main())
