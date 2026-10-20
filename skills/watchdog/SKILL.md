# Watchdog skill — v1.0

## Purpose and scope
Prevent wasteful agent loops, repeated failed actions, oscillation, and false claims of progress. This is a **framework-level checkpoint protocol** executed when the assistant regains control. It is **not** an independent process, timer, or guarantee that a stalled inference or hung tool call can be interrupted. A real runtime watchdog must be implemented in the execution environment to enforce hard timeouts.

## Progress evidence
Before a multi-step execution, identify the current task, intended outcome, and an observable progress signal (e.g. passing test, changed file verified by readback, new artifact, resolved blocker, or completed acceptance criterion). Record a short action ledger when practical: action type, target, relevant input fingerprint, outcome, error signature, evidence, and next action. Never treat repeated narrative or tool-call count alone as progress.

## Default trigger thresholds (adjust to risk and task)
- **Same failure twice** with unchanged prerequisites or equivalent inputs: suspected stall. Do not attempt a third identical retry.
- **Three consecutive actions without a measurable change** in task state: checkpoint. Legitimate batch work with distinct outputs is not a stall.
- **Two back-and-forth reversals** between approaches without new evidence: suspected oscillation.
- **Five tool/implementation actions** since the last checkpoint: briefly review progress, even if no failure occurred.
- Honor any stricter task-specific time, cost, retry, or turn budget. If no budget was agreed, avoid claiming one exists. These are heuristic checkpoints, not hard real-time interrupts.

Compare normalized intent, targets, inputs, preconditions, errors, and outcomes; do not infer duplication merely because two calls use the same tool. A repeated operation is legitimate when its input or environment changed or it advances a distinct item.

## Response to a suspected stall
1. **Pause the affected operation** at the next control point. Do not erase successful work or interrupt unrelated safe tasks.
2. State the expected outcome versus observed evidence and identify the repeated pattern or missing progress.
3. Check prerequisites, permissions, environment, requirements, and tool outputs. Distinguish transient failure from deterministic failure.
4. Select **one materially different recovery**: fix a prerequisite, narrow the operation, use a deterministic check, change the method, revert the failed attempt, or request missing authorization/information.
5. Define what observable evidence would prove recovery, then perform at most **two bounded recovery attempts**. Do not count a cosmetically rewritten identical action as a new strategy.
6. If still blocked, **stop the affected task**. Persist the last verified state, attempted approaches, exact blocker, and safe next action. Report it as BLOCKED or UNSYNCED as appropriate. Ask the user only for a decision they can actually resolve.

## False-positive protections
- Distinct test cases, pagination, batch processing, iterative refinement with measurable improvement, and authorized long-running jobs are not automatically loops.
- Do not disclose hidden reasoning or fabricate a background self-monitor. A short external progress summary is sufficient.
- Never bypass approval boundaries, spend money, alter permissions, or perform destructive operations as a recovery tactic without the required authorization.
- Never mark a stalled or unverified task COMPLETE.

## Continuity and reporting
For material stalls, record in `project/state.md` or `project/tasks.md`: task ID, trigger, last verified progress, error signature, attempted distinct recoveries, status, and next safe step. Avoid logging credentials or sensitive content. If repository writes fail, clearly label the record UNSYNCED.
At ordinary milestones report only useful outcomes; surface watchdog details when a stall affects progress or requires a user decision.

## Runtime extension (optional, separate)
A true independent watchdog can be added to an external agent runner using monotonic deadlines, tool-call cancellation where supported, heartbeat/progress events, durable state, and process isolation. This document alone cannot observe hidden model thinking, enforce wall-clock timeouts, or keep monitoring after the chat ends.
