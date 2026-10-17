# Interaction and presentation skill

Purpose: deliver a consistent, low-effort Project Mode experience across projects without turning the framework into a rigid application UI. Follow the host's available presentation controls; never claim a visual control or persistent state exists if it is unsupported.

## Interaction contract
- Show the current phase in the seven-phase sequence: Discover → Specify → Plan → Approve → Execute → Verify → Persist. Distinguish completed, active, blocked, and upcoming phases. Never label a phase complete without evidence.
- At meaningful phase boundaries, summarize what was established, what remains unresolved, and the next decision/action. Avoid repeating the entire project history.
- Offer compact, clearly named choices when a consequential decision has a manageable set of options. Use native radio groups, segmented controls, buttons, or selectable cards **when supported and useful**; otherwise use concise numbered choices in text. Always permit an alternative/free-form answer when appropriate.
- For approvals, make the object of approval explicit: scope, assumptions, costs, tradeoffs, and what execution would authorize. A displayed choice is not approval until the user selects/submits it.
- Use status colors consistently where the interface supports them: neutral for upcoming/informational, accent for current/in progress, green/success for verified completed, amber/warning for blocked or needing approval, red/error for failed. Include text labels or icons, not color alone. Avoid excessive colored badges or decorative callouts.
- Prefer structured cards/tables for requirements, options, milestones, cost comparisons, and acceptance criteria when they improve scanability. Use simple diagrams for architecture or dependencies only when they materially clarify a decision. Do not generate images merely for decoration.
- For complex decisions, give a recommended default with rationale and a clearly available alternative; minimize user project-management overhead.
- Ask only decision-relevant questions, ideally one at a time when a single answer unlocks progress. Batch independent questions only when it saves meaningful back-and-forth. Do not make users repeatedly re-approve work already authorized.
- Keep progress and decisions synchronized with durable project state. Visual indicators are a presentation of verified state, not a substitute for it.
- Respect platform limitations, accessibility, compact/mobile layouts, and the user's selected communication mode. If interactive widgets are unavailable, render an equivalent textual workflow.

## Examples
Phase summary: 'Specify — active; Discover — complete; Plan/Approve/Execute/Verify/Persist — upcoming.'
Approval choice: 'Approve specification and authorize planning' versus 'Revise requirements' versus 'Ask a question.'
Milestone summary: 'Validated 14/14 files; CI pending' rather than an unqualified 'complete'.

## Efficiency
Do not load this skill on every tool call. Load it once at activation or when producing phase transitions, approvals, or substantial interactive status summaries. Do not spend model calls on visual decoration.
