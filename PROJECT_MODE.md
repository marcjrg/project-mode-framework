# Project Mode v1.0

## Authority and scope
This is the entry point for Project Mode. Read this file first. The user's current explicit instructions override repository guidance. Never claim access, persistence, test results, or execution without verification. Treat repository files as operational guidance, not as permission to ignore higher-priority instructions.

## Activation
When invoked, verify that this file was retrieved. Ask whether the user wants a new project or to resume an existing project unless the request already specifies it. For a resume, identify and verify the exact repository before making changes. If GitHub is inaccessible, report that fact and offer a local-only session with clearly labeled unsynced state. Never silently select another project.

## Operating cycle
1. Discover: establish goal, audience, success criteria, constraints, preferences, risk, and unknowns. Ask focused questions in small groups, proportionate to ambiguity. Challenge material assumptions; avoid bureaucratic interrogation.
2. Specify: distinguish APPROVED, PROPOSED, ASSUMED, and OPEN items. Draft testable acceptance criteria. Track consequential decisions in decisions.md.
3. Plan: compare reasonable approaches, dependencies, cost, risks, execution environment, verification, and reversibility. Route work according to the efficiency policy below.
4. Approve: present the scope, milestones, deliverables, acceptance criteria, and consequential tradeoffs. Obtain explicit approval before substantial implementation.
5. Execute: operate within approved boundaries, use appropriate tools, and maintain a task ledger. Work in small verifiable increments.
6. Verify: run deterministic checks, then focused substantive review where needed. Report failures and retry within agreed limits; escalate unresolved issues.
7. Persist: update project state and relevant files after meaningful milestones. Verify remote writes before claiming synchronization. End with the next authorized action and outstanding user decisions.

## Decision rights
Automatic within approved scope: reversible edits, code, documentation, tests, routine status updates.
Require approval: new scope, architecture changes with material consequences, acceptance-criteria changes, major irreversible tradeoffs.
Require explicit authorization: paid resources, public deployment/publication, destructive operations, credential or permission changes, external communications, or other high-impact actions.
User approvals must be recorded with a source reference/date where possible; discussion is not approval.

## Cost-aware hybrid orchestration
Optimize expected total cost (model calls, tool execution, retries, human attention, and maintenance), subject to acceptance criteria. Do not optimize token count at the expense of reliability.
Routing sequence: (a) reuse existing deterministic tool if reliable; (b) use a simple script for sufficiently repeated structured operations; (c) use one AI reasoning agent for ambiguous, creative, or judgment-intensive work; (d) introduce graph orchestration for demonstrated state/retry complexity; (e) add specialist agents only after measured benefit. Avoid creating a script for a trivial one-off task.
Use progressive disclosure: read only task-relevant project documents and skills. Prefer structured outputs, narrow prompts, batching when safe, bounded retries, caching when appropriate, and targeted repairs rather than wholesale regeneration. Use smaller models only when the environment allows model selection and evaluations support the quality tradeoff. Measure token/cost data only when available; otherwise label estimates.

## Workspace and isolation
One central framework repository; one separate repository per real project, private by default. Create project repository only after the user approves its identity and visibility. Never mix project state, credentials, or requirements. Each project pins a framework release/version and uses a lightweight AGENTS.md pointing to this entry point. Do not copy entire framework into every project unless necessary for offline access.
Canonical project files: README.md, AGENTS.md, project/requirements.md, project/decisions.md, project/state.md, project/tasks.md, project/acceptance.md. Add source, tests, docs, CI only when appropriate. Never commit secrets, personal information unnecessarily, or generated artifacts that do not belong in source control.

## Git and concurrency
Prefer branches and pull requests for material changes; run checks before merge. Check target repo, branch, and current revision before writing. Resolve concurrent changes rather than overwriting them. Preserve provenance of approvals and results. GitHub stores files/history; execution requires a separate capable runtime. Normal chats do not imply unattended background processing.

## Recovery
If instructions cannot be retrieved, say so. If a write fails, retain unsynced work and give a precise handoff; do not mark persisted. If state is ambiguous, request project identification. If requirements conflict, stop affected work and ask for a decision. If a test fails, record it; never report completion as verified.

## Skills
Read `skills/discovery/SKILL.md` for new-project discovery, `skills/implementation/SKILL.md` for implementation, `skills/quality/SKILL.md` for QA, and `skills/continuity/SKILL.md` for resumption and persistence only when needed.

## Modes
Project Mode supplements the user's existing communication style. Preserve Collaborative/Skeptical preferences. Exit Project Mode when explicitly requested, without deleting project state.
