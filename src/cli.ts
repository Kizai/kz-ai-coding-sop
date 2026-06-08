#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

type CopyResult = {
  created: number;
  skipped: number;
};

const cwd = process.cwd();
const packageRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

const requiredFiles = [
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
  ".kz/sop.config.json"
];

const superpowersSkills = [
  "using-superpowers",
  "brainstorming",
  "writing-plans",
  "test-driven-development",
  "systematic-debugging",
  "verification-before-completion",
  "requesting-code-review",
  "subagent-driven-development",
  "executing-plans"
];

const gitignoreMarker = "KZ AI Coding SOP local runtime files";
const gitignoreBlock = [
  "# KZ AI Coding SOP local runtime files",
  ".ai/cache/",
  ".ai/tmp/",
  ".ai/logs/",
  ".ai/session/",
  ".kz/cache/",
  ".kz/tmp/",
  ""
].join("\n");

function copyDir(src: string, dest: string): CopyResult {
  const result: CopyResult = { created: 0, skipped: 0 };

  if (!fs.existsSync(src)) {
    return result;
  }

  fs.mkdirSync(dest, { recursive: true });

  for (const item of fs.readdirSync(src, { withFileTypes: true })) {
    const srcPath = path.join(src, item.name);
    const destPath = path.join(dest, item.name);

    if (item.isDirectory()) {
      const nested = copyDir(srcPath, destPath);
      result.created += nested.created;
      result.skipped += nested.skipped;
      continue;
    }

    if (fs.existsSync(destPath)) {
      result.skipped += 1;
      continue;
    }

    fs.mkdirSync(path.dirname(destPath), { recursive: true });
    fs.copyFileSync(srcPath, destPath);
    result.created += 1;
  }

  return result;
}

function appendGitignore(): boolean {
  const gitignorePath = path.join(cwd, ".gitignore");
  const current = fs.existsSync(gitignorePath)
    ? fs.readFileSync(gitignorePath, "utf8")
    : "";

  if (current.includes(gitignoreMarker)) {
    return false;
  }

  const prefix = current.length === 0 ? "" : current.endsWith("\n") ? "\n" : "\n\n";
  fs.appendFileSync(gitignorePath, `${prefix}${gitignoreBlock}`, "utf8");
  return true;
}

function detectStack(): string {
  const files = new Set(fs.readdirSync(cwd));

  if (files.has("next.config.js") || files.has("next.config.ts")) {
    return "nextjs";
  }

  if (files.has("vite.config.ts") || files.has("vite.config.js")) {
    return "react-node";
  }

  if (files.has("pyproject.toml") || files.has("requirements.txt")) {
    return "python-fastapi";
  }

  if ([...files].some((file) => file.endsWith(".csproj"))) {
    return "dotnet";
  }

  if (files.has("wp-config.php")) {
    return "wordpress";
  }

  return "base";
}

function init(): void {
  const stack = detectStack();
  const baseTemplate = path.join(packageRoot, "templates", "base");
  const stackTemplate = path.join(packageRoot, "templates", stack);

  const baseResult = copyDir(baseTemplate, cwd);
  const stackResult = stack === "base" ? { created: 0, skipped: 0 } : copyDir(stackTemplate, cwd);
  const gitignoreUpdated = appendGitignore();
  const created = baseResult.created + stackResult.created;
  const skipped = baseResult.skipped + stackResult.skipped;

  console.log(`KZ AI Coding SOP initialized.

Detected stack: ${stack}
Created files: ${created}
Skipped existing files: ${skipped}
.gitignore updated: ${gitignoreUpdated ? "yes" : "no"}

Next prompt for your coding agent:

Please follow KZ AI Coding SOP for this project.
First read AGENTS.md and .ai/AGENT_ENTRY.md.
Do not write code immediately.
Start by reporting project understanding, stack detection, structure analysis, plan, relevant Superpowers skills, risks, and verification steps.
`);
}

function doctor(): number {
  let ok = true;

  console.log("KZ AI Coding SOP doctor\n");

  for (const file of requiredFiles) {
    const exists = fs.existsSync(path.join(cwd, file));
    if (!exists) {
      ok = false;
    }
    console.log(`${exists ? "[ok]" : "[missing]"} ${file}`);
  }

  console.log("\nSuperpowers integration:");
  console.log("- Confirm Superpowers is installed in each agent harness you use.");
  console.log("- KZ SOP does not auto-install third-party plugins.");
  console.log("- Upstream: https://github.com/obra/superpowers");

  return ok ? 0 : 1;
}

function listKzSkills(): string[] {
  const skillsDir = path.join(packageRoot, "skills");

  if (!fs.existsSync(skillsDir)) {
    return [];
  }

  return fs
    .readdirSync(skillsDir, { withFileTypes: true })
    .filter((item) => item.isDirectory())
    .map((item) => item.name)
    .filter((name) => fs.existsSync(path.join(skillsDir, name, "SKILL.md")))
    .sort();
}

function listSkills(): void {
  console.log("Recommended upstream Superpowers skills:");
  for (const skill of superpowersSkills) {
    console.log(`- superpowers:${skill}`);
  }

  const kzSkills = listKzSkills();
  console.log("\nPackaged KZ-owned skills:");
  if (kzSkills.length === 0) {
    console.log("- none");
    return;
  }

  for (const skill of kzSkills) {
    console.log(`- ${skill}`);
  }
}

function help(): void {
  console.log(`KZ AI Coding SOP

Usage:
  kz-sop init
  kz-sop update
  kz-sop doctor
  kz-sop skills list
`);
}

const command = process.argv[2] ?? "help";

switch (command) {
  case "init":
  case "update":
    init();
    break;
  case "doctor":
    process.exitCode = doctor();
    break;
  case "skills":
    if (process.argv[3] === "list") {
      listSkills();
    } else {
      console.log("Usage: kz-sop skills list");
      process.exitCode = 1;
    }
    break;
  case "help":
  case "--help":
  case "-h":
    help();
    break;
  default:
    help();
    process.exitCode = 1;
}
