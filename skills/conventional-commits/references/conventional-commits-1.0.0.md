# Conventional Commits 1.0.0 reference

This reference condenses the Conventional Commits 1.0.0 specification supplied by the user in `convention commit.pdf`. It preserves the normative message structure while adding practical decision guidance. The public specification is available at <https://www.conventionalcommits.org/en/v1.0.0/>.

## Message grammar

```text
<type>[optional scope][optional !]: <description>

[optional body]

[optional footer(s)]
```

Examples:

```text
feat(auth): add password reset flow
```

```text
fix(parser): preserve spaces inside quoted values

Avoid trimming tokens before the quoted-value parser runs.

Refs: #133
```

```text
feat(api)!: remove the legacy authentication endpoint

BREAKING CHANGE: clients must use OAuth 2.0 tokens.
```

## Normative structural rules

1. Start with a type. A scope in parentheses and `!` are optional. End the prefix with `: `.
2. Use `feat` for a new capability and `fix` for a defect correction.
3. When present, the scope is a noun naming the affected area, such as `api`, `parser`, or `auth`.
4. A non-empty short description must follow the prefix.
5. A body may add context and begins after one blank line.
6. One or more footers may follow the body after one blank line.
7. A footer uses a token followed by `: ` or ` #`. Replace spaces in ordinary footer tokens with `-`, for example `Reviewed-by`. `BREAKING CHANGE` is the exception.
8. A breaking change is marked by `!` immediately before `:` and/or an uppercase `BREAKING CHANGE: description` footer. `BREAKING-CHANGE` is an accepted footer synonym.
9. Types other than `feat` and `fix` are allowed. Their SemVer meaning is defined by the project, except that any breaking change is major.
10. Parsers must treat structural units case-insensitively except for the uppercase `BREAKING CHANGE` token. For consistency and ecosystem compatibility, prefer lowercase types.

The specification does not impose a header-length limit, imperative mood, English language, issue identifier, or fixed list of additional types. A repository may add those rules.

## Common type vocabulary

Use repository-defined types first. When none exist, this vocabulary is a practical default:

| Type | Use when the commit primarily... | Default SemVer effect |
|---|---|---|
| `feat` | adds user-visible or API capability | minor |
| `fix` | corrects incorrect behavior | patch |
| `docs` | changes documentation only | none |
| `test` | adds or corrects tests without product behavior changes | none |
| `refactor` | restructures code without changing intended behavior | none |
| `perf` | improves performance without changing intended behavior | project-defined |
| `style` | changes formatting without changing behavior | none |
| `build` | changes build system or dependencies | project-defined |
| `ci` | changes CI configuration or scripts | none |
| `chore` | performs maintenance not better described elsewhere | none |
| `revert` | reverses earlier work | project-defined |

Do not use `chore` as a generic escape hatch when a more informative type applies.

## Type and scope decision

Ask in order:

1. Does it introduce a capability? Use `feat`.
2. Does it repair behavior that was wrong? Use `fix`.
3. Does it change behavior only through performance? Consider `perf`.
4. Does it preserve behavior while changing structure? Use `refactor`.
5. Is it limited to tests, documentation, formatting, build, or CI? Use the matching type.
6. Is it truly routine maintenance with no clearer category? Use `chore`.

Use a scope only when it adds stable context. Prefer a domain, module, service, or subsystem name already used by the repository. Avoid filenames, temporary task names, and redundant scopes.

## Description, body, and footers

- The description states the outcome, not the activity: `fix(api): reject expired tokens` is more useful than `fix(api): update token code`.
- Keep one intent per subject. If the sentence needs "and" to join unrelated outcomes, consider multiple commits.
- Use the body to explain why, constraints, tradeoffs, or behavior that is not obvious from the diff.
- Use footers for traceability and machine-readable metadata, such as `Refs: #133` or `Reviewed-by: Name`.
- Never claim a breaking change merely because an internal implementation changed. It must break a supported consumer contract.

## Atomicity

A good atomic commit:

- expresses one coherent reason for change;
- contains the implementation and directly coupled tests or documentation needed to keep that intent complete;
- can be reviewed and reverted without dragging unrelated work with it;
- does not separate files that are jointly required for one behavior;
- does not combine refactoring, feature work, and incidental cleanup unless they are inseparable.

When a change fits more than one type, split it where practical. Examples include preparatory refactoring followed by a feature, or an independent defect fix discovered during feature work.

## SemVer mapping

- `fix` maps to a PATCH release.
- `feat` maps to a MINOR release.
- Any type with a breaking-change marker maps to a MAJOR release.
- Other types have no implicit SemVer effect unless project tooling defines one.

This mapping communicates release impact; it does not itself publish a release.

## Reverts and corrections

The base specification leaves revert semantics to tooling. A common form is:

```text
revert: restore the previous authentication flow

Refs: 676104e, a215868
```

Before merge or release, an incorrect local message can be corrected through an explicitly authorized history-editing workflow. After publication, do not rewrite history by default; follow the repository's release and recovery process.
