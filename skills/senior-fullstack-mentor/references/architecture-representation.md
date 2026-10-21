# Effective Architecture Representation

Architecture documentation exists to support decisions and shared understanding. Prefer a small, maintained set of views over one exhaustive diagram or a large document that drifts from reality.

## Start with audience and question

Before drawing, identify:

- who will use the representation;
- what decision or task it must support;
- which system boundary and level of detail matter;
- whether it describes observed current state, a proposal, or verified implementation;
- what evidence can keep it honest.

Do not create a diagram merely because a process expects one. Do not combine business context, source-code structure, data details, runtime infrastructure, and request timing in a single view.

## Select the minimum useful views

Use C4 as a practical structural vocabulary, not as ceremony:

1. **System context:** people, the system of interest, external systems, and named relationships. Use it to explain scope, ownership, and dependencies.
2. **Containers:** deployable applications, processes, data stores, queues, and their protocols. Use it as the default technical overview.
3. **Components:** major responsibilities inside one container. Add it only when internal boundaries influence the decision or implementation.
4. **Code:** classes and low-level structure. Prefer source navigation and generated documentation; draw this view only for a specific difficult mechanism.

Add complementary views only when they answer a question the structural views cannot:

- **Sequence or flow:** ordering, state transitions, retries, timeouts, partial failures, and asynchronous behavior.
- **Data model:** ownership, identities, relationships, cardinality, invariants, retention, and compatibility.
- **Deployment:** environments, processes, network zones, trust boundaries, scaling, storage, and external dependencies.
- **ADR:** context, alternatives, choice, consequences, and triggers for revisiting a consequential decision.

## Content rules

Each view should include:

- title, scope, audience or purpose, status, and last verified date when useful;
- a legend when notation is not obvious;
- named elements with one clear responsibility;
- named relationships that describe direction, intent, and protocol when relevant;
- system, ownership, data, or trust boundaries that affect the task;
- only the technology details that influence a decision;
- links or pointers to the relevant code, configuration, contract, ADR, or operational evidence when available.

Use consistent names across diagrams, code, deployment, and operational documentation. Mark uncertainty rather than silently filling gaps.

## Evidence states

Keep these states explicit and separate:

- **Observed current:** derived from inspected code, configuration, schemas, or runtime evidence; cite the evidence and note gaps.
- **Proposed:** a target or option that is not yet implemented; include assumptions, consequences, migration, and validation criteria.
- **Verified implemented:** matched against the delivered code and proportionate execution evidence. State whether verification was local, automated, connected, or production-level.

Never use a target-state diagram as proof of the current system. When current and proposed states differ materially, use separate diagrams rather than ambiguous colors alone.

## Architecture workflow

1. Define the capability, audience, scope, and evidence state.
2. Inspect the actual system before documenting current state.
3. Draw context and containers first for cross-boundary work.
4. Add the smallest complementary view needed for the decision.
5. Identify contracts, data ownership, failure paths, trust boundaries, and operational responsibilities.
6. Compare alternatives using the architecture decision method.
7. Record consequential choices in an ADR.
8. Validate names and relationships against code and configuration.
9. Update the relevant views in the same change that alters architectural boundaries.

## Quality check

A representation is effective when a reader can answer:

- What is inside and outside the scope?
- Who owns each important responsibility and data set?
- How do the important parts communicate?
- Where can the critical flow fail, and how is failure observed or recovered?
- Which facts are current, which are proposed, and which remain uncertain?
- Why was this design chosen, and what would trigger reconsideration?

Remove detail that does not help answer these questions. Split a view when it requires excessive zoom, crossed relationships, or mixed abstraction levels.

## Maintenance

Prefer text-based or repository-native diagrams when the team can maintain them reliably, but do not impose a tool. The source of truth is the combination of code, configuration, contracts, runtime evidence, and recorded decisions; diagrams are navigational models of that truth.

Treat a stale diagram as a defect in the affected documentation. Update only the views influenced by a change instead of redrawing the entire architecture.
