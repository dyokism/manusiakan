#!/usr/bin/env python3
"""Check Manusiakan's package files without external dependencies."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def read_package_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as error:
        raise SystemExit(f"Cannot read {path.relative_to(ROOT)}: {error}")


SKILL_PATH = ROOT / "SKILL.md"
SKILL = read_package_file(SKILL_PATH)
README = read_package_file(ROOT / "README.md")
CHANGELOG = read_package_file(ROOT / "CHANGELOG.md")
try:
    PLUGIN = json.loads(read_package_file(ROOT / ".claude-plugin" / "plugin.json"))
except json.JSONDecodeError as error:
    raise SystemExit(f"Fix the JSON in .claude-plugin/plugin.json: {error}")


def require_match(match: re.Match[str] | None, message: str) -> re.Match[str]:
    if match is None:
        raise SystemExit(message)
    return match


yaml_metadata = require_match(
    re.match(r"\A---\n(.*?)\n---\n", SKILL, re.DOTALL),
    "SKILL.md must begin with YAML metadata",
).group(1)

for unsupported_field in ("version:", "compatibility:", "allowed-tools:"):
    if re.search(rf"(?m)^{re.escape(unsupported_field)}", yaml_metadata):
        raise SystemExit(f"Remove unsupported YAML field: {unsupported_field[:-1]}")

skill_version = require_match(
    re.search(
        r'(?m)^\s+version:\s*["\']?([0-9]+\.[0-9]+\.[0-9]+)["\']?\s*$', yaml_metadata
    ),
    "Add metadata.version to SKILL.md as a three-part version",
).group(1)
changelog_version = require_match(
    re.search(r"(?m)^## ([0-9]+\.[0-9]+\.[0-9]+)$", CHANGELOG),
    "Add a version heading to CHANGELOG.md",
).group(1)

package_versions = {
    skill_version,
    changelog_version,
    str(PLUGIN.get("version", "")),
}
if len(package_versions) != 1:
    raise SystemExit(
        f"Use one package version in all files: {sorted(package_versions)}"
    )

skill_files = {path.relative_to(ROOT) for path in ROOT.rglob("SKILL.md")}
if SKILL_PATH.is_symlink() or skill_files != {Path("SKILL.md")}:
    raise SystemExit("Keep one regular SKILL.md at the repo root")
if PLUGIN.get("skills") != ["./"]:
    raise SystemExit("Point the Claude plugin skill loader at the repo root")

skill_description = " ".join(
    require_match(
        re.search(r"(?m)^description: \|\n((?:  .*\n)+)", yaml_metadata + "\n"),
        "Write the SKILL.md description as an indented block",
    ).group(1).split()
)
MARKETPLACE = json.loads(
    read_package_file(ROOT / ".claude-plugin" / "marketplace.json")
)
package_descriptions = {
    str(PLUGIN.get("description", "")),
    *(str(plugin.get("description", "")) for plugin in MARKETPLACE.get("plugins", [])),
}
if len(package_descriptions) != 1 or not skill_description.startswith(
    next(iter(package_descriptions))
):
    raise SystemExit(
        "Use the first sentence of the SKILL.md description in every plugin manifest: "
        f"{sorted(package_descriptions)}"
    )

# Every word of SKILL.md is read on each use, so the budget is in words.
skill_words = len(SKILL.split())
if skill_words > 5500:
    raise SystemExit(f"Keep SKILL.md at 5,500 words or fewer; it has {skill_words}")

print(f"Manusiakan package v{skill_version} is valid ({skill_words} words)")
