---
name: mui-template-frontend
description: Select, integrate, and adapt the official free Material UI React templates for dashboards, marketing pages, checkout, authentication, blogs, and CRUD interfaces. Use when a React project should start from or reuse parts of the MUI template collection. Do not use to copy premium MUI Store templates or for projects that are not using Material UI.
---

# MUI Template Frontend

Turn an official Material UI template into a project-specific starting point without treating demo code as finished product code.

## Authorization and companion skills

Inspect freely, but do not edit, install packages, run migrations, commit, publish, or deploy without the user's authorization.

When the companion skills are installed:

1. Use `senior-fullstack-mentor` for scope, engineering decisions, and authorization mode.
2. Use this skill for MUI template selection and integration.
3. Use `design-taste-frontend` only for marketing, portfolio, and brand-facing surfaces. It is not the design authority for dashboards, data tables, or multi-step product flows.
4. Use `conventional-commits` after validation to propose or create atomic commits. A request for a message is not authorization to commit.

## Establish the starting point

Before choosing a template, identify:

- the page job: dashboard, marketing, checkout, sign-in, sign-up, blog, or CRUD;
- whether this is greenfield, an integration into an existing React app, or a redesign;
- the framework and versions in `package.json`, plus the active lockfile;
- the current router, theme provider, styling engine, authentication boundary, and data layer;
- which content, routes, analytics hooks, field names, and brand assets must remain stable.

If the project already exists, inspect before proposing package or architecture changes. Never assume the latest documentation matches the installed major version.

## Use official sources

Check the current [Material UI template catalog](https://mui.com/material-ui/getting-started/templates/) and its linked source before implementation. Read [references/template-catalog.md](references/template-catalog.md) to map the request to a template and [references/integration-workflow.md](references/integration-workflow.md) before changing a project.

Use free template source from the official `mui/material-ui` repository. Do not reproduce, scrape, or bypass access controls for premium MUI Store templates. Verify the upstream license and dependency versions when vendoring code.

## Select the smallest useful template

Choose by the dominant user flow, not by visual similarity alone:

- Dashboard for data visualization and navigation-heavy product UI.
- Marketing page for product positioning, testimonials, pricing, and FAQs.
- Checkout for staged purchase or onboarding forms.
- Sign-in, sign-in side, or sign-up for authentication entry points.
- Blog for content-led homepages and Markdown-backed publishing.
- CRUD dashboard for record management with responsive navigation.

Extract only the page sections and shared theme pieces the project needs. Do not import an entire demo when one component or layout is sufficient.

## Integrate as project code

Preserve the project's conventions unless the user approves a migration. In particular:

- keep one component system; do not mix MUI with another full design system;
- install only dependencies required by the selected template and chosen components;
- adapt the upstream shared theme into semantic project tokens instead of scattering demo colors;
- replace mock data, sample links, placeholder identities, and no-op handlers;
- isolate authentication, payments, persistence, and API calls behind real project boundaries;
- preserve route slugs, analytics identifiers, form names, and legal copy during redesigns;
- retain upstream notices required by the current license.

Treat comments such as "docs-only" and preview-frame offsets as candidates for removal after confirming they are not used by the target app.

## Validate at real boundaries

Validate the adapted result in proportion to its risk:

- run the repository's existing typecheck, lint, and tests;
- build the production bundle;
- exercise the page at mobile, tablet, and desktop widths;
- test keyboard navigation, focus visibility, labels, error messages, and color contrast;
- verify light and dark schemes only when both are part of the accepted scope;
- test loading, empty, error, and success states using real component boundaries;
- verify route changes, form submission, authentication redirects, and data mutations where applicable;
- compare against the original user requirements, not merely the MUI demo.

Do not claim production readiness from a successful render alone. Distinguish source review, local execution, automated validation, and connected-environment testing.

## Delivery

Report:

- the selected template and why it fits;
- upstream source and version or commit when known;
- files adapted versus copied;
- dependencies added or removed;
- validation actually performed;
- remaining placeholders, external integrations, and uncertainties;
- a proposed atomic commit plan, without committing unless explicitly authorized.
