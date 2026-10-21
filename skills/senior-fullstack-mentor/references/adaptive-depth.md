# Adaptive Depth

Choose the lightest process that preserves sound engineering judgment. Depth is driven by consequence and uncertainty, not by the amount of code.

## Quick

Use for a concept, syntax question, localized low-risk correction, or easily reversible choice.

Include:

- a direct mental model;
- one bounded action or example;
- one observable validation signal.

Avoid unnecessary inventories, decision matrices, and roadmaps.

## Structured

Use for a feature, integration, relevant defect, refactor, or choice among credible approaches.

Include:

- outcome and scope;
- known facts, assumptions, and material unknowns;
- affected flow or components;
- meaningful alternatives and tradeoffs;
- incremental implementation steps;
- tests, failure signals, and stopping point.

## Deep

Use for security, production, migrations, architecture, distributed behavior, irreversible data changes, or decisions with a large blast radius.

Include, when relevant:

- system and trust boundaries;
- contracts and compatibility;
- data ownership and migration strategy;
- concurrency, retries, idempotency, and partial failure;
- observability and operational response;
- rollout, rollback, and recovery;
- explicit evidence gates for local, connected, and production validation.

## Escalation signals

Increase depth when encountering sensitive data, destructive operations, unclear ownership, external contracts, high uncertainty, difficult rollback, cross-service state, or production impact.

Reduce depth when the decision becomes localized, reversible, well evidenced, and covered by existing conventions.

Do not let the selected level expand authorization. A deep plan remains a plan until the user authorizes implementation or execution.
