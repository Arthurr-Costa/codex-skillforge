# Grounded Solution Exploration

Use this method when a problem has multiple credible solutions and the choice affects maintainability, architecture, operations, or learning. Skip it for small tasks with an obvious adequate answer.

## Separate divergence from convergence

During divergence, generate materially different approaches rather than cosmetic variations:

- **Conservative:** preserve the current design and make the smallest useful change.
- **Balanced:** improve the design while limiting migration and operational cost.
- **Bold:** challenge an important constraint or structure only when the possible gain justifies investigation.
- **Defer:** gather evidence, contain the problem, or leave the system unchanged for now.

Not every task needs all four. Never invent a complex option merely to fill the list.

During convergence, test each viable option against:

1. confirmed evidence and explicit assumptions;
2. fit with existing contracts and project conventions;
3. implementation and cognitive complexity;
4. operational burden and failure modes;
5. security and data consequences;
6. reversibility and rollback cost;
7. ability to validate locally and in the relevant environment;
8. value delivered relative to effort;
9. learning value for the user.

## Recommendation contract

State:

- the recommended option;
- the decisive reasons;
- the strongest rejected alternative and why it lost;
- what evidence could change the recommendation;
- the smallest next step that reduces uncertainty.

Prefer an incremental path when it preserves future options. A creative proposal is not a decision until it survives constraints and has a credible validation path.

## Guardrails

- Do not replace the user's chosen stack without a concrete benefit.
- Do not introduce distributed components, dependencies, abstractions, or patterns only for elegance.
- Do not confuse novelty with quality.
- Do not describe an inference as a confirmed fact.
- Do not optimize a dimension that the task does not materially depend on.
- When evidence is weak, recommend an experiment rather than a structural commitment.
