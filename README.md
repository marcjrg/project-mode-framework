# Project Mode Framework v1.0

A lightweight, approval-driven, GitHub-backed operating framework for AI-assisted projects. Start with [PROJECT_MODE.md](PROJECT_MODE.md). This repository contains operating rules, specialized skills, project templates, and deterministic validation scripts.

## Activation
In ChatGPT custom instructions, set `"Project Mode"` to retrieve and follow `https://github.com/marcjrg/project-mode-framework/blob/main/PROJECT_MODE.md`. Explicitly report retrieval failure instead of assuming instructions. Preserve existing Collaborative or Skeptical Mode preferences.

## Response format
Every Project Mode reply starts with a concise executive-summary paragraph: verified progress or answer, current status/next step, and the exact action required from the user (or an explicit **no action needed**). See [PROJECT_MODE.md](PROJECT_MODE.md) and [skills/interaction/SKILL.md](skills/interaction/SKILL.md).

## Project workspaces
Use `templates/` to initialize a **separate private repository per project**, after explicit approval. GitHub is the durable store; coding/build execution requires an appropriate runtime. Repository creation, read/write access, and cross-chat retrieval must each be verified; they are not guaranteed by the framework itself.

## Validation
Run `python scripts/validate.py .` from the repository root. Python 3.10+ is sufficient. No third-party dependencies. GitHub Actions also runs the validation script on push and pull requests.

## Security
Do not store secrets in repository files. Use least-privilege GitHub permissions. Public framework repositories must not contain personal project state.
