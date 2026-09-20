---
name: conventional-commits
description: Guide, propose, validate, and optionally create atomic Git commits that follow Conventional Commits 1.0.0. Use when the user asks for a commit message, commit plan, semantic commit review, commit splitting, SemVer impact, or execution of Git commits. Do not use for general code review or release-note writing unless commit semantics are part of the request.
---

# Conventional Commits

Help the user understand both what to commit and why. Default to analysis and teaching; do not create, amend, rewrite, push, or otherwise mutate Git history unless the user explicitly requests that operation.

## Source of truth

Read [references/conventional-commits-1.0.0.md](references/conventional-commits-1.0.0.md) before generating or evaluating an exact commit message. Apply repository-specific rules when they are stricter than the base specification.

## Choose the operating mode

- **Teach:** explain the convention, the appropriate type and scope, and the SemVer effect. Make no repository changes.
- **Propose:** inspect the current changes and produce an atomic commit plan with exact candidate messages. Make no repository changes.
- **Validate:** check supplied messages or existing commits and explain each violation. Make no repository changes.
- **Execute:** create only the commits explicitly authorized by the user. A request to explain, plan, review, or suggest is not authorization to commit.

When the user's wording is ambiguous, remain in Propose mode and state that no commit was created.

## Inspect before deciding

When a repository is available, gather read-only evidence before proposing a message:

1. Read applicable `AGENTS.md`, `CONTRIBUTING.md`, commit templates, commitlint configuration, release tooling, and package scripts.
2. Inspect `git status --short`, staged and unstaged diffs, and untracked file names. Never print secrets or `.env` contents.
3. Review a small sample of recent commit subjects to learn the repository's language, scopes, and accepted types. Treat history as convention evidence, not proof that every old message is valid.
4. Separate unrelated work. One commit should represent one coherent intent and remain independently understandable and reversible.

Do not assume all dirty files belong to the requested commit. Preserve user changes that are outside the selected intent.

## Build the commit plan

For each proposed commit, explain:

- the single intent;
- the files or hunks that belong to it;
- the chosen `type` and optional `scope`;
- whether a body or footer is useful;
- the exact message;
- the expected SemVer effect, if any;
- the evidence or validation appropriate before committing.

If one change fits multiple types, prefer splitting it when each part can stand alone. Do not split mechanically by file when files jointly implement one behavior.

Match the repository's established natural language unless the user specifies another. Keep machine-significant tokens such as `feat`, `fix`, and `BREAKING CHANGE` in their required Conventional Commits form.

## Validate candidate messages

Run the bundled validator for every exact message produced when shell execution is available:

```bash
python3 scripts/validate_commit_message.py --message 'feat(api): add retry policy'
```

For multiline messages, use a file or standard input. The validator checks the portable 1.0.0 structure; repository hooks may impose additional constraints.

Do not invent ticket identifiers, co-authors, reviewers, breaking changes, or scopes. Ask for missing identifiers only when the repository requires them; otherwise omit them.

## Execute safely

Enter this mode only after an explicit request to create the commit or commits.

1. Restate the approved grouping and inspect the current status again because the worktree may have changed.
2. Stage only the approved paths or hunks. Do not replace, discard, or unstage pre-existing user work without explicit permission.
3. Review `git diff --cached` and validate the final message before committing.
4. Respect project hooks. Never use `--no-verify` unless the user explicitly requests it and understands the consequence.
5. Create one commit per approved intent. Stop if the staged content no longer matches the plan, a hook fails, or new ambiguity appears.
6. Report the commit hash, exact subject, included scope, validation performed, and any remaining changes.

Commit authorization never implies permission to push, deploy, amend another commit, rebase, reset, force-push, or rewrite published history. Those operations require separate explicit authorization.

## Response quality

Lead with the recommendation. Teach the decision rule briefly enough that the user can apply it next time. Clearly distinguish:

- proposed versus created commits;
- staged versus unstaged content;
- specification errors versus optional style preferences;
- Conventional Commits validity versus repository-specific policy.
