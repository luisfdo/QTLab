# QTLab Domain Model

## Status
Approved

---

## Purpose
This document defines the conceptual model of QTLab.

It describes the concepts that exist within the domain of quantitative research and the relationships between them.

The purpose of this document is not to describe software implementation.

Its purpose is to establish a shared understanding of the language, responsibilities and boundaries of the domain.

The domain model is implementation-independent.

---

## Domain Philosophy
QTLab models research, not trading.

Its central concern is the creation, evaluation and preservation of knowledge.

Experiments are performed to generate evidence.

Evidence supports assessments.

Assessments contribute to knowledge.

Knowledge generates new questions.

The domain therefore models a continuous cycle of investigation rather than a linear execution pipeline.

---

## The Knowledge Cycle

        Observation
             │
             ▼
    Research Question
             │
             ▼
       Hypothesis
             │
             ▼
       Methodology
             │
             ▼
       Experiment
             │
             ▼
         Evidence
             │
             ▼
       Assessment
             │
             ▼
        Reflection
             │
             ▼
    New Observations

A completed Study may produce one or more new observations, creating the next cycle of research.

---

## Core Aggregate

### Study
The Study is the central aggregate of the QTLab domain.

A Study represents one investigation into one research question.

Everything else belongs to a Study.

A Study is the primary unit of reproducibility.

### Responsibilities
A Study:

- defines the research context;
- owns the research artifacts;
- records the investigation history;
- preserves reasoning;
- maintains reproducibility.

### Invariants
A Study:

- investigates exactly one Research Question;
- contains at least one Observation;
- may contain multiple Experiments;
- produces zero or more Evidence artifacts;
- may conclude with an Assessment;
- may contain a Reflection;
- may generate new Studies.

---

## Knowledge Artifacts
Knowledge artifacts capture the intellectual progress of a Study.

They are durable, versionable and explainable.

### Observation
An Observation records something noticed by the researcher.

It motivates the Study.

An Observation should describe **what was noticed**, not why it happened.

---

## Research Question
The Research Question transforms curiosity into a testable objective.

Every Study investigates exactly one Research Question.

A good Research Question is:

- specific;
- measurable;
- answerable through evidence.

---

## Hypothesis
A Hypothesis proposes an explanation or prediction.

A Hypothesis should be falsifiable.

A Study may revise its Hypothesis as evidence accumulates.

Hypothesis revisions remain part of the Study history.

---

## Methodology
A Methodology defines how the hypothesis will be investigated.

It specifies:

- assumptions;
- datasets;
- experiment design;
- parameters;
- evaluation criteria.

Methodologies are reusable across Studies.

---

## Evidence
Evidence represents interpreted experimental results.

Evidence is not raw data.

Evidence summarizes observations supported by experiments.

Evidence may support or contradict the Hypothesis.

Contradictory evidence is considered equally valuable.

---

## Assessment
The Assessment records the researcher's current interpretation of the evidence.

An Assessment represents the best current understanding.

It is not considered absolute truth.

Future evidence may invalidate previous assessments.

---

## Reflection
Reflection captures what the researcher learned while conducting the Study.

It records:

surprises;

limitations;

lessons learned;

future questions.

Reflection is optional but encouraged.

---

## Activities
Activities produce knowledge.

### Experiment
An Experiment executes a Methodology.

Its purpose is to generate Evidence.

Experiments are repeatable.

Every Experiment should be reproducible.

Experiments are implementation details from the perspective of the domain.

Their value lies in the knowledge they produce.

---

## Supporting Concepts

### Dataset
A Dataset represents the information used by Experiments.

Datasets describe:

- provenance;
- coverage;
- quality;
- limitations.

Datasets are shared resources.

Studies reference datasets.

They do not own them.

---

## Research Timeline
The Research Timeline records significant events within a Study.

Examples:

- Observation recorded;
- Hypothesis revised;
- Experiment executed;
- Assessment updated.

The Timeline preserves the evolution of reasoning.

---

## States
A Study may exist in one of the following states.

- Under Investigation
- Waiting for Evidence
- Needs Review
- Assessment Ready
- Completed
- Archived

States describe research progress.

They do not imply success or failure.

---

## Relationships

    Study
    
    ├── Observation 
    ├── Research Question
    ├── Hypothesis
    ├── Methodology
    ├── Experiment *
    ├── Evidence *
    ├── Assessment
    ├── Reflection
    └── Timeline *

(*) indicates zero or more instances.

---

## Domain Rules

### Research precedes execution
A Study should establish its Question and Hypothesis before running Experiments.

### Evidence precedes Assessment
Assessments should be based upon Evidence.

### Contradictory Evidence is preserved
Negative or unexpected findings are never discarded.

### Reproducibility is mandatory
Every Experiment must be reproducible using the recorded Methodology and Dataset.

### Reasoning is preserved
Changes in research direction remain part of the permanent Study history.

### Ubiquitous Language
The terms defined in this document are part of the ubiquitous language of QTLab.

Future domain concepts should integrate with this language rather than introducing competing terminology.

---

## Future Evolution
Future generations may extend this model with concepts such as:

- Collaboration
- AI Assistant
- Research Pipeline
- Knowledge Graph
- Publications
- Peer Review
- Live Studies

These additions must preserve the integrity of the Study as the central aggregate.
