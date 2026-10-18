# Install Project Mode in Your Own GitHub Account

**Installer entry point.** This document is intended to be read and executed by an AI assistant after a user asks it to install Project Mode. It is a procedure, not permission to perform actions without user authorization.

## Goal
Create an independent, private-by-default copy of this public Project Mode framework in the user's **own** GitHub account, verify the copy, and give the user short, personalized activation instructions for their AI assistant. The source repository is `marcjrg/project-mode-framework`. **Never write to the source repository.**

## First response to the new user

Before starting setup or requesting GitHub authorization, give the user a **short, friendly, plain-language explanation** of what they are receiving. Use wording like this, adapting naturally:

> **Project Mode** is a reusable way to turn ChatGPT into a structured project partner. It helps you plan a project, make decisions, track progress, and check results without having to manage every step yourself. It can show clear progress stages and simple choices when supported.
>
> I'm going to help you create **your own private copy** of the framework in GitHub. You can customize it independently, and it won't give anyone else permission to change your projects. I'll handle the setup where my tools allow it and ask you only for necessary permissions or decisions.

Keep this opening to approximately 80–120 words or fewer. Avoid technical jargon, a long feature list, or implying the framework itself guarantees access to external tools. **Do not claim the repository has already been created.** Then begin installation by checking the user's GitHub connection and asking for the required repository-creation approval. If the guide is inaccessible or capabilities are missing, explain that before promising installation.

## Installer procedure

1. **Read and inventory source.** Retrieve this guide, `PROJECT_MODE.md`, `AGENTS.md`, `README.md`, and the repository's full tracked file tree on the default branch. Retrieve every tracked file's bytes, including all `skills/`, `templates/`, `scripts/`, `.github/`, and any future directories; do not rely on a fixed filename list. Capture the source commit SHA. Exclude `.git/` metadata and any user-specific secrets if discovered; pause and explain any unexpected sensitive data. If the environment cannot enumerate and copy all files, say so and request an appropriate tool/connection rather than silently making a partial copy.
2. **Identify destination and authorize.** Determine the signed-in user's GitHub account through the connected GitHub integration. Do not assume the source owner is the destination owner. Propose a private repository named `project-mode-framework` (or an available user-chosen name). Explicitly request approval to create it, including its name, owner, and visibility. If it already exists, do **not** overwrite: offer a new name or ask for a separately approved, non-destructive import strategy.
3. **Check capabilities.** Confirm that the available tools can create repositories, write files, and verify reads. A GitHub read-only connection is insufficient. If installation/permissions are missing, guide the user through connecting the **official** GitHub/Codex integration and selecting their own repository; do not suggest arbitrary Marketplace apps. If the AI environment cannot create or write repositories, offer a user-approved GitHub **Use this template** flow (if the source is designated as a template) or a one-time manual import with clear limitations. Never claim full automation where tools do not support it.
4. **Create and copy.** After approval, create the destination as **private** unless the user explicitly chooses otherwise. Copy all tracked framework files, preserving paths, content, and executable bits where the tools support them. Use bounded retries for transient errors; record any failures. Preserve license and attribution notices if present. Do not copy repository settings, secrets, collaborators, or tokens. GitHub Actions workflow files may require additional permissions; report any inability to copy them.
5. **Personalize.** In the destination copy only, replace references used for *activation* and *self-installation* with the user's actual `https://github.com/OWNER/REPO` address. Preserve upstream credit in a small 'Origin' section in the destination README, and optionally link to upstream for updates. Do not make the installed framework depend on reading the original repo. Update `INSTALL.md`'s source reference if the user wants to redistribute their customized copy, but do not accidentally redirect attribution.
6. **Verify.** Compare the destination's complete tracked file inventory with the source inventory (allowing intentional personalization). Read back important files, including `PROJECT_MODE.md`, `INSTALL.md`, `skills/interaction/SKILL.md`, and `scripts/validate.py`. Run `python scripts/validate.py .` when an execution runtime is available; otherwise state that the validation script was not executed. Check destination visibility is private and record destination commit SHA. Distinguish successful writes from passing CI.
7. **Handoff.** Give the user their exact destination repository URL and this ready-to-copy custom-instructions snippet, substituting the actual verified `OWNER/REPO`:

```text
PROJECT MODE

"Project Mode" = Retrieve and follow https://github.com/OWNER/REPO/blob/main/PROJECT_MODE.md and its relevant linked skills. Use its workflow, interaction standards, approvals, and continuity rules. If retrieval fails, tell me instead of guessing.

"Exit Project Mode" = Return to my usual interaction style.
```

Tell the user to paste it into ChatGPT **Settings → Personalization → Custom Instructions** (or the equivalent setting in another AI). Explain that private repository retrieval requires that AI account to have authorized read access; do not assume public browser access will work. Ask them to test `Project Mode` in a new conversation and verify it retrieves their copy.

## Completion standard
Only report 'installed' after destination creation, complete file copy, successful read-back, and confirmed private visibility. Otherwise report the exact blocker and the next minimal action. Never claim to have changed ChatGPT account settings on the user's behalf. Do not create project-specific repositories as part of this installer.

## Short prompt to share
> Install Project Mode for me using https://github.com/marcjrg/project-mode-framework/blob/main/INSTALL.md. Handle setup; ask only when my approval or action is required.
