from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CWD = Path.cwd()

REQUIRED_FILES = [
    "AGENTS.md",
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

GITIGNORE_MARKER = "KZ AI Coding SOP generated files"
GITIGNORE_BLOCK = "\n".join(
    [
        "# KZ AI Coding SOP generated files",
        ".kz/",
        "AGENTS.md",
        "",
    ]
)


def copy_dir(
    src: Path, dest: Path, overwrite: bool = False
) -> tuple[int, int, int, list[str]]:
    created = 0
    refreshed = 0
    skipped = 0
    refreshed_paths: list[str] = []

    if not src.exists():
        return created, refreshed, skipped, refreshed_paths

    for item in src.rglob("*"):
        if item.is_dir():
            continue

        relative = item.relative_to(src)
        target = dest / relative

        if target.exists():
            if not overwrite or target.read_bytes() == item.read_bytes():
                skipped += 1
                continue

            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, target)
            refreshed += 1
            refreshed_paths.append(str(relative))
            continue

        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, target)
        created += 1

    return created, refreshed, skipped, refreshed_paths


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


NEXT_PROMPT = """Next prompt for your coding agent:

Please follow KZ AI Coding SOP for this project.
First read AGENTS.md.
Do not write code immediately.
Start by reporting project understanding, stack detection, structure analysis, plan, relevant Superpowers skills, risks, and verification steps."""


def init(mode: str = "init") -> int:
    overwrite = mode == "update"
    stack = detect_stack()

    base_template = ROOT / "templates" / "base"
    if not base_template.exists():
        print(
            f"KZ AI Coding SOP template directory is missing: {base_template}",
            file=sys.stderr,
        )
        return 1

    base_created, base_refreshed, base_skipped, base_paths = copy_dir(
        base_template, CWD, overwrite
    )
    if stack == "base":
        stack_created, stack_refreshed, stack_skipped, stack_paths = 0, 0, 0, []
    else:
        stack_created, stack_refreshed, stack_skipped, stack_paths = copy_dir(
            ROOT / "templates" / stack, CWD, overwrite
        )

    gitignore_updated = append_gitignore()

    created = base_created + stack_created
    refreshed = base_refreshed + stack_refreshed
    skipped = base_skipped + stack_skipped
    refreshed_paths = base_paths + stack_paths

    if mode == "update":
        refreshed_list = f" ({', '.join(refreshed_paths)})" if refreshed_paths else ""
        print(
            f"""KZ AI Coding SOP updated.

Detected stack: {stack}
Refreshed files: {refreshed}{refreshed_list}
Created files: {created}
Unchanged files: {skipped}
.gitignore updated: {"yes" if gitignore_updated else "no"}

{NEXT_PROMPT}
"""
        )
    else:
        print(
            f"""KZ AI Coding SOP initialized.

Detected stack: {stack}
Created files: {created}
Skipped existing files: {skipped}
.gitignore updated: {"yes" if gitignore_updated else "no"}

{NEXT_PROMPT}
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
        return init(command)

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
