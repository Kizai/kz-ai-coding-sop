from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CWD = Path.cwd()

REQUIRED_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    ".ai/AGENT_ENTRY.md",
    ".ai/CORE_RULES.md",
    ".ai/CODING_STANDARD.md",
    ".ai/ARCHITECTURE_STANDARD.md",
    ".ai/WORKFLOW.md",
    ".ai/SKILL_INDEX.md",
    ".ai/REVIEW_CHECKLIST.md",
    ".cursor/rules/kz-ai-rules.mdc",
    ".kz/sop.config.json",
]

SUPERPOWERS_SKILLS = [
    "using-superpowers",
    "brainstorming",
    "writing-plans",
    "test-driven-development",
    "systematic-debugging",
    "verification-before-completion",
    "requesting-code-review",
    "subagent-driven-development",
    "executing-plans",
]

GITIGNORE_MARKER = "KZ AI Coding SOP local runtime files"
GITIGNORE_BLOCK = "\n".join(
    [
        "# KZ AI Coding SOP local runtime files",
        ".ai/cache/",
        ".ai/tmp/",
        ".ai/logs/",
        ".ai/session/",
        ".kz/cache/",
        ".kz/tmp/",
        "",
    ]
)


def copy_dir(src: Path, dest: Path) -> tuple[int, int]:
    created = 0
    skipped = 0

    if not src.exists():
        return created, skipped

    for item in src.rglob("*"):
        if item.is_dir():
            continue

        relative = item.relative_to(src)
        target = dest / relative

        if target.exists():
            skipped += 1
            continue

        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, target)
        created += 1

    return created, skipped


def append_gitignore() -> bool:
    gitignore = CWD / ".gitignore"
    current = gitignore.read_text(encoding="utf-8") if gitignore.exists() else ""

    if GITIGNORE_MARKER in current:
        return False

    prefix = "" if not current else "\n" if current.endswith("\n") else "\n\n"
    with gitignore.open("a", encoding="utf-8") as file:
        file.write(f"{prefix}{GITIGNORE_BLOCK}")

    return True


def detect_stack() -> str:
    files = {item.name for item in CWD.iterdir()}

    if "next.config.js" in files or "next.config.ts" in files:
        return "nextjs"

    if "vite.config.ts" in files or "vite.config.js" in files:
        return "react-node"

    if "pyproject.toml" in files or "requirements.txt" in files:
        return "python-fastapi"

    if any(name.endswith(".csproj") for name in files):
        return "dotnet"

    if "wp-config.php" in files:
        return "wordpress"

    return "base"


def init() -> int:
    stack = detect_stack()

    base_created, base_skipped = copy_dir(ROOT / "templates" / "base", CWD)
    if stack == "base":
        stack_created, stack_skipped = 0, 0
    else:
        stack_created, stack_skipped = copy_dir(ROOT / "templates" / stack, CWD)

    gitignore_updated = append_gitignore()

    print(
        f"""KZ AI Coding SOP initialized.

Detected stack: {stack}
Created files: {base_created + stack_created}
Skipped existing files: {base_skipped + stack_skipped}
.gitignore updated: {"yes" if gitignore_updated else "no"}

Next prompt for your coding agent:

Please follow KZ AI Coding SOP for this project.
First read AGENTS.md and .ai/AGENT_ENTRY.md.
Do not write code immediately.
Start by reporting project understanding, stack detection, structure analysis, plan, relevant Superpowers skills, risks, and verification steps.
"""
    )
    return 0


def doctor() -> int:
    ok = True
    print("KZ AI Coding SOP doctor\n")

    for file in REQUIRED_FILES:
        exists = (CWD / file).exists()
        if not exists:
            ok = False
        print(f"{'[ok]' if exists else '[missing]'} {file}")

    print("\nSuperpowers integration:")
    print("- Confirm Superpowers is installed in each agent harness you use.")
    print("- KZ SOP does not auto-install third-party plugins.")
    print("- Upstream: https://github.com/obra/superpowers")

    return 0 if ok else 1


def list_kz_skills() -> list[str]:
    skills_dir = ROOT / "skills"

    if not skills_dir.exists():
        return []

    return sorted(
        item.name
        for item in skills_dir.iterdir()
        if item.is_dir() and (item / "SKILL.md").exists()
    )


def list_skills() -> int:
    print("Recommended upstream Superpowers skills:")
    for skill in SUPERPOWERS_SKILLS:
        print(f"- superpowers:{skill}")

    print("\nPackaged KZ-owned skills:")
    kz_skills = list_kz_skills()
    if not kz_skills:
        print("- none")
        return 0

    for skill in kz_skills:
        print(f"- {skill}")

    return 0


def help_text() -> str:
    return """KZ AI Coding SOP

Usage:
  kz-sop init
  kz-sop update
  kz-sop doctor
  kz-sop skills list
"""


def main() -> int:
    command = sys.argv[1] if len(sys.argv) > 1 else "help"

    if command in {"init", "update"}:
        return init()

    if command == "doctor":
        return doctor()

    if command == "skills":
        if len(sys.argv) > 2 and sys.argv[2] == "list":
            return list_skills()
        print("Usage: kz-sop skills list")
        return 1

    if command in {"help", "--help", "-h"}:
        print(help_text())
        return 0

    print(help_text())
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
