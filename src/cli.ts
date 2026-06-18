#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

type CopyResult = {
  created: number;
  refreshed: number;
  skipped: number;
  refreshedPaths: string[];
};

const cwd = process.cwd();
const packageRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

const requiredFiles = [
  "AGENTS.md",
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

const gitignoreMarker = "KZ AI Coding SOP generated files";
const gitignoreBlock = [
  "# KZ AI Coding SOP generated files",
  ".kz/",
  "AGENTS.md",
  ""
].join("\n");

function copyDir(src: string, dest: string, overwrite = false): CopyResult {
  const result: CopyResult = { created: 0, refreshed: 0, skipped: 0, refreshedPaths: [] };

  if (!fs.existsSync(src)) {
    return result;
  }

  fs.mkdirSync(dest, { recursive: true });

  for (const item of fs.readdirSync(src, { withFileTypes: true })) {
    const srcPath = path.join(src, item.name);
    const destPath = path.join(dest, item.name);

    if (item.isDirectory()) {
      const nested = copyDir(srcPath, destPath, overwrite);
      result.created += nested.created;
      result.refreshed += nested.refreshed;
      result.skipped += nested.skipped;
      result.refreshedPaths.push(...nested.refreshedPaths);
      continue;
    }

    if (fs.existsSync(destPath)) {
      if (!overwrite || fs.readFileSync(srcPath).equals(fs.readFileSync(destPath))) {
        result.skipped += 1;
        continue;
      }

      fs.mkdirSync(path.dirname(destPath), { recursive: true });
      fs.copyFileSync(srcPath, destPath);
      result.refreshed += 1;
      result.refreshedPaths.push(path.relative(cwd, destPath));
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

const nextPrompt = `Next prompt for your coding agent:

Please follow KZ AI Coding SOP for this project.
First read AGENTS.md.
Do not write code immediately.
Start by reporting project understanding, stack detection, structure analysis, plan, relevant Superpowers skills, risks, and verification steps.`;

function init(mode: "init" | "update"): void {
  const overwrite = mode === "update";
  const stack = detectStack();
  const baseTemplate = path.join(packageRoot, "templates", "base");
  const stackTemplate = path.join(packageRoot, "templates", stack);

  if (!fs.existsSync(baseTemplate)) {
    console.error(`KZ AI Coding SOP template directory is missing: ${baseTemplate}`);
    process.exitCode = 1;
    return;
  }

  const baseResult = copyDir(baseTemplate, cwd, overwrite);
  const stackResult =
    stack === "base"
      ? { created: 0, refreshed: 0, skipped: 0, refreshedPaths: [] }
      : copyDir(stackTemplate, cwd, overwrite);
  const gitignoreUpdated = appendGitignore();
  const created = baseResult.created + stackResult.created;
  const refreshed = baseResult.refreshed + stackResult.refreshed;
  const skipped = baseResult.skipped + stackResult.skipped;
  const refreshedPaths = [...baseResult.refreshedPaths, ...stackResult.refreshedPaths];

  if (mode === "update") {
    const refreshedList = refreshedPaths.length === 0 ? "" : ` (${refreshedPaths.join(", ")})`;
    console.log(`KZ AI Coding SOP updated.

Detected stack: ${stack}
Refreshed files: ${refreshed}${refreshedList}
Created files: ${created}
Unchanged files: ${skipped}
.gitignore updated: ${gitignoreUpdated ? "yes" : "no"}

${nextPrompt}
`);
    return;
  }

  console.log(`KZ AI Coding SOP initialized.

Detected stack: ${stack}
Created files: ${created}
Skipped existing files: ${skipped}
.gitignore updated: ${gitignoreUpdated ? "yes" : "no"}

${nextPrompt}
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
    init(command);
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
