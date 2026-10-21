# Durable recording and resumption

## Minimum useful record

Adapt to the note's language and existing headings. A compact paragraph can satisfy this contract; do not force a new template on every note.

- Objective and relevant context: what the user is trying to achieve.
- Material outcome or decision: what actually changed or was agreed.
- Evidence and limits: files, commits, artifacts, sources or observed results; distinguish what remains unverified.
- Pending work or blocker: unresolved items with owners and dates only if known.
- Next action: an observable step that lets the user resume.

Use the existing project/area note as the canonical state. Add a compact dated entry with a wikilink to the established activity log. If no activity log convention exists, a dated section in the project note is enough; ask before creating an elaborate new hierarchy. Daily notes and dashboards are navigation aids, not additional copies of the full record.

A request to record only a short note can be fulfilled with that note alone. User-selected scope and privacy preferences prevail.

## Evidence language

Separate these states explicitly when they affect the conclusion:

| State | Meaning |
|---|---|
| Planned | Idea, proposal or agreed next step; not implemented |
| Implemented | Source or artifact changed; execution may still be pending |
| Validated locally | A bounded local check ran with its stated result |
| Validated in a connected environment | The specific authenticated integration or environment was observed |
| Delivered or production-proven | Publication, handoff or production result was actually confirmed |

These are evidence qualifiers, not a mandatory replacement for the user's status vocabulary. A locally passing test does not establish successful deployment. A sent commit does not establish installation. A saved note does not establish visual rendering. Record only the strongest demonstrated claim and retain the missing gate.

## Safe editing and duplication

Read the exact note and relevant activity section immediately before editing. Preserve user text, frontmatter types, unchecked tasks, headings and native date notes. Apply a narrow edit; do not replace an entire note with a freshly generated summary.

Search for the same outcome, commit or artifact before adding another entry. Update existing tasks and add only the new milestone. On a repeated run with no new evidence or state change, make no duplicate entry. When evidence contradicts a prior claim, explain the correction and preserve the historical trail rather than silently upgrading or deleting it.

Re-read after writing and check that links and new status statements match the saved contents. If a connector or filesystem write fails, stop repeated unchanged retries, preserve a concise pending record in the response, and identify the exact missing access or capability. Never mark recording as complete based only on an attempted write.

## Resuming and closing

At resumption, read the canonical note and affected pending items, then inspect fresh source/runtime evidence for facts likely to have changed. Show the next useful action, not a dump of every historical entry. Reconcile only tasks affected by the current evidence.

At daily closure, inspect the native daily note in place and only accessible evidence. Do not claim global chat coverage when only a subset was read. Leave inactive days alone. A background closure or reminder requires separate explicit user authorization; this reference does not create a schedule.

## Example of proportional closure

User implements a login change and local tests pass, but the portal is unavailable. Update the existing project note with the implemented change and passing local checks, retain authenticated portal validation as pending, set the next action to retry that named journey when access is available, and append one short linked log entry. Do not mark the integration delivered or schedule a retry on your own.
