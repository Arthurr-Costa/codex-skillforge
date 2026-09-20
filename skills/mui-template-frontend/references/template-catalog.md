# Official template catalog

Use this file as a routing aid, then verify the live catalog because names, dependencies, and implementation details can change.

## Free templates observed on 2026-09-20

| Template | Best fit | Important checks |
|---|---|---|
| Dashboard | Analytics, monitoring, and data-heavy product areas | MUI X package requirements, licensing tier, responsive navigation, real data states |
| Marketing page | Product landing pages | Brand tokens, content quality, image assets, conversion paths, restrained component repetition |
| Checkout | Purchase or staged onboarding | Validation, step persistence, payment boundary, recovery, mobile completion |
| Sign-in | Compact authentication entry | Provider integration, error handling, password recovery, redirect safety |
| Sign-in side | Authentication plus supporting brand or product content | Same auth checks plus responsive collapse and meaningful media |
| Sign-up | Account creation | Field validation, consent, verification flow, duplicate accounts, error recovery |
| Blog | Content-led homepage with Markdown support | Content source, sanitization, routing, metadata, accessibility |
| CRUD dashboard | Record management | API contracts, authorization, optimistic updates, pagination, empty and error states |

The official catalog states that free templates provide custom and default Material themes with light and dark modes, and that sections are separated for reuse. This does not mean every project must keep both themes or every section.

## Canonical sources

- Catalog: <https://mui.com/material-ui/getting-started/templates/>
- Source root: <https://github.com/mui/material-ui/tree/master/docs/data/material/getting-started/templates>
- Shared theme: <https://github.com/mui/material-ui/tree/master/docs/data/material/getting-started/templates/shared-theme>
- Installation: <https://mui.com/material-ui/getting-started/installation/>
- Theming: <https://mui.com/material-ui/customization/theming/>
- Responsive UI: <https://mui.com/material-ui/guides/responsive-ui/>

## Selection rules

1. Match the template to the main user task.
2. Prefer the smallest extractable surface.
3. Check package compatibility before copying files.
4. Use MUI X only when the feature requires it and its current license fits the project.
5. Treat premium MUI Store material as out of scope unless the user supplies licensed source code.
