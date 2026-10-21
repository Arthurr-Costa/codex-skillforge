# Working With Unfamiliar Technology

Use this protocol when the task involves a language, framework, library, platform, version, or runtime not covered by the skill's focused references or not known with sufficient confidence.

## Epistemic contract

Do not present general programming knowledge as verified technology-specific behavior. Label information as one of:

- observed in the project;
- confirmed by authoritative documentation;
- inferred from related concepts;
- unknown and requiring verification.

## Investigation sequence

1. Identify the exact technology, version, runtime, and task boundary when available.
2. Inspect the project's manifests, configuration, conventions, tests, and nearby working examples.
3. Determine which parts are stable principles and which depend on version-specific behavior.
4. Consult primary or official documentation when behavior, syntax, compatibility, security, or current APIs matter.
5. Form the smallest useful mental model: input, lifecycle, state, side effects, errors, and observability.
6. Build a minimal, isolated, reversible experiment when documentation and project evidence are insufficient.
7. Update the recommendation from the observed result.

Do not browse or run experiments when the answer is already safely established and the task is low risk. Do not add packages or modify the project merely to explore without the required authorization.

## Transfer from known concepts

Reason by explicit analogy, then verify the technology-specific details. Useful bridges include:

- types and contracts;
- request and event lifecycles;
- dependency and module boundaries;
- state, concurrency, and consistency;
- persistence and transactions;
- error propagation and recovery;
- build, test, and deployment pipelines.

Say where the analogy may break. For example, similar-looking async models may have different scheduling, cancellation, or error semantics.

## Output

Provide the user with:

- what is confirmed;
- what remains uncertain;
- the working model being used;
- the next verification step;
- a recommendation proportional to the evidence.

If authoritative evidence cannot be obtained, keep the answer conditional and avoid production-safety claims.
