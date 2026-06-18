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
            self.assertIn(".kz", gitignore)
            self.assertIn("AGENTS.md", gitignore)
            self.assertNotIn(".kz/cache/", gitignore)
            self.assertNotIn(".kz/tmp/", gitignore)
            self.assertNotIn(".ai/cache/", gitignore)
            self.assertNotIn(".ai/tmp/", gitignore)

    def test_gitignore_appends_core_paths_to_existing_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            gitignore = tmp_path / ".gitignore"
            gitignore.write_text("node_modules/\n", encoding="utf-8")

            result = run_cli("init", cwd=tmp_path)
            content = gitignore.read_text(encoding="utf-8")

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(content.startswith("node_modules/\n"))
            self.assertIn("# KZ AI Coding SOP generated files", content)
            self.assertIn(".kz", content)
            self.assertIn("AGENTS.md", content)

    def test_skills_list_includes_karpathy_guidelines(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            result = run_cli("skills", "list", cwd=tmp_path)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("- karpathy-guidelines", result.stdout)

    def test_skills_list_includes_newly_packaged_skills(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            result = run_cli("skills", "list", cwd=tmp_path)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("- ralph-loop", result.stdout)
            self.assertIn("- planning-with-files", result.stdout)
            self.assertIn("- spec-driven-development", result.stdout)

    def test_update_refreshes_modified_core_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            run_cli("init", cwd=tmp_path)

            agents_md = tmp_path / "AGENTS.md"
            packaged = (ROOT / "templates" / "base" / "AGENTS.md").read_text(
                encoding="utf-8"
            )
            agents_md.write_text("locally edited\n", encoding="utf-8")

            result = run_cli("update", cwd=tmp_path)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("KZ AI Coding SOP updated.", result.stdout)
            self.assertIn("Refreshed files: 1 (AGENTS.md)", result.stdout)
            self.assertEqual(agents_md.read_text(encoding="utf-8"), packaged)

    def test_update_is_noop_when_core_files_match(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            run_cli("init", cwd=tmp_path)

            result = run_cli("update", cwd=tmp_path)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Refreshed files: 0", result.stdout)
            self.assertIn("Unchanged files: 2", result.stdout)
            self.assertIn(".gitignore updated: no", result.stdout)


if __name__ == "__main__":
    unittest.main()
