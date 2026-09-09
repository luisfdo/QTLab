# QTLab Generation 1 Product Specification

## Status
Approved

---

## Mission
Generation 1 exists to prove that quantitative research can be structured, reproducible and enjoyable.

Its objective is not to build the most feature-rich backtesting engine.

Its objective is to enable a researcher to conduct one complete Study from an initial observation to a well-supported assessment while preserving the reasoning behind every decision.

Generation 1 establishes the foundation upon which all future generations of QTLab will evolve.

---

## Product Vision
QTLab is not a trading platform.

It is not a charting application.

It is not an automated strategy generator.

QTLab is an engineering environment for quantitative research.

It helps researchers transform curiosity into structured knowledge.

---

## Target Audience
Generation 1 is designed primarily for:

### Primary Personas
#### Experienced Retail Traders
Researchers who already formulate trading ideas but lack a structured and reproducible research process.

#### Quantitative Researchers
Researchers who value scientific methodology, reproducibility and documentation as much as numerical results.

---

## Secondary Personas
Software engineers interested in systematic trading.

Graduate students learning quantitative finance.

Open-source contributors interested in research infrastructure.

---

## Product Philosophy
Generation 1 follows five principles.

1. Research before software
QTLab should encourage scientific thinking before technical implementation.

2. Reasoning is a first-class artifact
The "why" behind a decision is as valuable as the experiment itself.

3. Evidence before conclusions
QTLab produces evidence.

Researchers produce assessments.

4. Reproducibility is mandatory
Every completed Study must be reproducible months or years later.

5. Curiosity drives the workflow
The first interaction with QTLab begins with an observation, not with data or code.

---

## Success Criteria
Generation 1 is considered complete when an independent researcher can:

- create a Study,
- formulate a research question,
- define a hypothesis,
- select a methodology,
- execute an experiment,
- review the resulting evidence,
- write an assessment,
- optionally record a reflection,
- reproduce the Study from scratch.

---

## Non-Goals
Generation 1 intentionally excludes:

- live trading
- broker integration
- portfolio management
- optimization engines
- AI-generated strategies
- cloud execution
- collaboration
- multi-user support
- plugin systems
- strategy marketplaces
- distributed execution
- online service deployment

These capabilities belong to future generations.

---

## Core Capability
Generation 1 delivers one capability:

>Complete one rigorous quantitative Study.

Everything else exists to support this capability.

---

## The Study
The Study is the primary user-facing artifact of QTLab.

A Study investigates one research question.

A Study contains:

- Observation
- Research Question
- Hypothesis
- Methodology
- Dataset
- Experiment
- Evidence
- Assessment
- Reflection (optional)

A Study may generate additional research questions.

Those questions become future Studies.

---

## Research Workflow
The canonical workflow is:

    Observation
    ↓
    Research Question
    ↓
    Hypothesis
    ↓
    Methodology
    ↓
    Experiment
    ↓
    Evidence
    ↓
    Assessment
    ↓
    Reflection

The workflow is iterative.

Evidence may require revisiting earlier stages.

Research is not assumed to be linear.

---

## Study States
A Study may exist in one of several states.

- Under Investigation
- Waiting for Evidence
- Needs Review
- Assessment Ready
- Completed
- Archived

A Study is not required to reach a final assessment.

Explicit uncertainty is a valid outcome.

---

## User Experience
Generation 1 follows a progressive workflow.

The researcher is never overwhelmed with unnecessary information.

Only information required for the current stage is presented.

The software should feel like guiding a scientific investigation rather than completing forms.

---

## The Research Canvas
Every Study is represented through a Research Canvas.

The Canvas displays the current state of every research stage.

The Canvas is the central navigation experience of QTLab.

Future generations may introduce additional visualizations such as Pipeline View or Timeline View without changing the underlying Study model.

Reference Study
Generation 1 ships with one Reference Study.

The Reference Study is not an example.

It is the benchmark against which all Generation 1 capabilities are evaluated.

Every feature introduced into Generation 1 must improve the experience of creating, executing or understanding the Reference Study.

The Reference Study demonstrates the complete lifecycle of a Study from Observation to Assessment.

---

## Deliverables
Generation 1 delivers:

- the Study model
- the Research Canvas
- one supported research methodology
- one supported market dataset
- experiment execution
- evidence generation
- assessment recording
- study reproducibility
- the Reference Study

---

## Design Principles
The interface should:

- encourage curiosity;
- minimize cognitive load;
- expose complexity progressively;
- preserve reasoning alongside results;
- communicate at the research level rather than the implementation level.

---

## Quality Principles
Every feature introduced into Generation 1 should satisfy at least one of the following:

- improves scientific rigor;
- improves reproducibility;
- reduces cognitive friction;
- improves documentation;
- improves understanding of the Study.

Features that satisfy none of these should not be included in Generation 1.

---

## Definition of Done
Generation 1 is complete when:

- a new user can complete the Reference Study without external assistance;
- another researcher can reproduce the Study and obtain equivalent results;
- the Study remains understandable months later;
- the experience encourages the researcher to begin a second Study.
