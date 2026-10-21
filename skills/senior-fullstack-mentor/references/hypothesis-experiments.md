# Hypothesis-Driven Experiments

Use this method when progress depends on an unverified explanation, especially in debugging, performance work, unfamiliar systems, and novel design ideas.

## Hypothesis record

Write the smallest useful version of:

```text
Observation:
What was actually seen?

Hypothesis:
What specific mechanism could explain it?

Current evidence:
What supports or weakens the hypothesis?

Experiment:
What is the smallest safe action that distinguishes this hypothesis from alternatives?

Confirms if:
What observable result increases confidence?

Refutes if:
What observable result rejects or materially weakens it?

Next decision:
What happens for either outcome?
```

## Experiment quality

A useful experiment:

- changes one important variable when practical;
- produces observable evidence rather than an impression;
- is cheap, bounded, and reversible;
- avoids production or destructive effects unless explicitly authorized and justified;
- has a stopping condition;
- distinguishes competing explanations.

Prefer logs, focused tests, minimal reproductions, query plans, controlled inputs, and isolated benchmarks over broad rewrites.

## Interpretation

One successful run rarely proves universal correctness. Record the environment, input, version, and scope of the observation. Separate:

- evidence consistent with the hypothesis;
- evidence that rules out alternatives;
- uncertainty that remains;
- generalization that still requires broader validation.

When an experiment refutes the hypothesis, treat that as progress. Update the model before proposing another change; do not retrofit the explanation to protect the original idea.
