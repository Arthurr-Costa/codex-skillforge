# Integration workflow

Read this reference before adapting an official MUI template into a project.

## 1. Inventory

Record the existing React framework, MUI version, Emotion setup, router, theme provider, test runner, lockfile, and relevant page boundaries. Identify user-owned changes before editing.

## 2. Source pinning

Record the upstream template URL and, when reproducibility matters, the Git commit or release tag used. The documentation website can move ahead of a project's installed major version.

## 3. Dependency delta

Compare imports in the selected template with `package.json`. Separate core dependencies from template-specific packages. For example, dashboard features may require MUI X packages and a date library that authentication templates do not need.

Do not install a package merely because it appears elsewhere in the template catalog.

## 4. Controlled extraction

Copy the selected page and only the supporting components it actually imports. Bring the shared theme primitives deliberately. Remove documentation preview wrappers and offsets only after tracing their use.

Keep an attribution note when required by the upstream license. Never copy premium template source without a valid user-provided license and source.

## 5. Project adaptation

Replace demo content and wiring in this order:

1. Routes and layout shell.
2. Semantic theme tokens and brand assets.
3. Real content and navigation.
4. Form validation and domain rules.
5. Authentication, APIs, persistence, or payments.
6. Loading, empty, error, and success states.
7. Analytics and observability hooks already used by the project.

Avoid a broad visual rewrite before the behavior and contracts are mapped.

## 6. Quality gates

Use the project's own commands when available. At minimum, verify type safety, linting, production build, keyboard behavior, responsive layouts, theme contrast, and the primary user flow.

For marketing pages, combine this workflow with `design-taste-frontend` and run its pre-flight checks. For dashboards and forms, prioritize task clarity, information density, validation, accessibility, and error recovery over marketing-page aesthetics.

## 7. Handoff evidence

List the exact commands and scenarios that passed, anything not run, upstream references, dependency changes, remaining mock content, and the proposed commit grouping.
