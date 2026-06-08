from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_cli(*args: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "kz_sop.cli", *args],
        cwd=cwd,
        env={"PYTHONPATH": str(ROOT)},
        text=True,
        capture_output=True,
        check=False,
    )


def all_files(root: Path) -> set[str]:
    return {
        str(path.relative_to(root))
        for path in root.rglob("*")
        if path.is_file()
    }


class InitCoreModeTest(unittest.TestCase):
    def test_init_creates_only_core_sop_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            result = run_cli("init", cwd=tmp_path)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(
                all_files(tmp_path),
                {
                    ".gitignore",
                    ".kz/sop.config.json",
                    "AGENTS.md",
                },
            )
            self.assertIn("Created files: 2", result.stdout)
            self.assertIn(".gitignore updated: yes", result.stdout)
            self.assertFalse((tmp_path / ".cursor").exists())
            self.assertFalse((tmp_path / ".ai").exists())
            self.assertFalse((tmp_path / "CLAUDE.md").exists())

    def test_init_is_idempotent_and_doctor_uses_core_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            first = run_cli("init", cwd=tmp_path)
            second = run_cli("init", cwd=tmp_path)
            doctor = run_cli("doctor", cwd=tmp_path)

            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual(doctor.returncode, 0, doctor.stdout)
            self.assertIn("Created files: 0", second.stdout)
            self.assertIn("Skipped existing files: 2", second.stdout)
            self.assertIn(".gitignore updated: no", second.stdout)
            self.assertIn("[ok] AGENTS.md", doctor.stdout)
            self.assertIn("[ok] .kz/sop.config.json", doctor.stdout)
            self.assertNotIn(".cursor/rules/kz-ai-rules.mdc", doctor.stdout)
            self.assertNotIn(".ai/AGENT_ENTRY.md", doctor.stdout)

    def test_gitignore_runtime_block_is_minimal(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            result = run_cli("init", cwd=tmp_path)
            gitignore = (tmp_path / ".gitignore").read_text(encoding="utf-8")

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn(".kz/cache/", gitignore)
            self.assertIn(".kz/tmp/", gitignore)
            self.assertNotIn(".ai/cache/", gitignore)
            self.assertNotIn(".ai/tmp/", gitignore)


if __name__ == "__main__":
    unittest.main()
