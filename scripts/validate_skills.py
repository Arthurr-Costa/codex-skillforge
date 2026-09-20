#!/usr/bin/env python3
"""Validate the portable structure of every skill in this repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def parse_frontmatter(text: str) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, ["missing YAML frontmatter opening"]

    try:
        raw_frontmatter, _body = text[4:].split("\n---\n", 1)
    except ValueError:
        return {}, ["missing YAML frontmatter closing"]

    fields: dict[str, str] = {}
    for line in raw_frontmatter.splitlines():
        if not line.strip() or line.startswith(" ") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"\'')

    for required in ("name", "description"):
        if not fields.get(required):
            errors.append(f"missing frontmatter field: {required}")
    return fields, errors


def validate_links(skill_file: Path, text: str) -> list[str]:
    errors: list[str] = []
    for target in LINK_PATTERN.findall(text):
        clean_target = target.split("#", 1)[0]
        if not clean_target or "://" in clean_target or clean_target.startswith("mailto:"):
            continue
        if not (skill_file.parent / clean_target).exists():
            errors.append(f"broken local link: {target}")
    return errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return ["missing SKILL.md"]

    text = skill_file.read_text(encoding="utf-8")
    fields, frontmatter_errors = parse_frontmatter(text)
    errors.extend(frontmatter_errors)

    declared_name = fields.get("name", "")
    if declared_name and not NAME_PATTERN.fullmatch(declared_name):
        errors.append(f"invalid skill name: {declared_name}")
    if "[TODO:" in text or "TODO: Add" in text:
        errors.append("unfinished TODO placeholder")

    errors.extend(validate_links(skill_file, text))

    metadata_file = skill_dir / "agents" / "openai.yaml"
    if metadata_file.is_file():
        metadata = metadata_file.read_text(encoding="utf-8")
        if "default_prompt:" in metadata and f"${declared_name}" not in metadata:
            errors.append("default_prompt does not mention the declared skill name")

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"ERROR: skills directory not found: {SKILLS_DIR}")
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    failures = 0
    for skill_dir in skill_dirs:
        errors = validate_skill(skill_dir)
        if errors:
            failures += 1
            print(f"FAIL {skill_dir.name}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {skill_dir.name}")

    print(f"\nValidated {len(skill_dirs)} skills; failures: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
