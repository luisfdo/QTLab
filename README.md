# QTLab

## Vision
QTLab aims to become the open-source operating system for quantitative investment research.
It enables researchers to transform market observations into evidence-based investment decisions through reproducible experiments and rigorous validation.

>It is not a trading bot, a signal generator, or a strategy optimizer. It is a platform that enables researchers to transform observations about financial markets into evidence-based investment decisions through disciplined experimentation, rigorous validation, and continuous learning.
>
>Every component in QTLab exists to answer one question:
> 
>**"What does the evidence tell us?"**

## Mission
**QTLab is an open-source quantitative research operating system
that helps researchers transform market observations into 
evidence-based investment decisions through reproducible experiments.**

## Coding Standards
Type hints everywhere:

    def load_csv(path: Path) -> pl.DataFrame:

**No untyped functions unless absolutely necessary.**


## Docstrings
 - Every public class.
 - Every public function.

**Not because Python needs them. Because future-us needs them.**


## Tests
Every module gets tested immediately.

Not "*we'll write tests later*". Never.


## Formatting
Automatic. No discussions!

Ruff + formatter.

## Documentation

Each document should answer *Why does this subsystem exist?*

not *What functions does it have?*

That's much more valuable.

## Project Vocabulary

| Prefix | Meaning                       |
|--------|-------------------------------|
| ADR    | Architecture Decision Record  |
| DS     | Dataset                       |
| EXP    | Experiment                    |
| HYP    | Research hypothesis           |
| QT     | QTLab engineering task        |
| RFC    | Request for Comments          |
| SPEC   | Functional specification      |
| TEST   | Acceptance or validation test |


## Workflow

                  MARKET
                     │
                     ▼
              Observation
                     │
                     ▼
            Research Question
                     │
                     ▼
               Hypothesis
                     │
                     ▼
               Experiment
                     │
         ┌───────────┴────────────┐
         ▼                        ▼
     Validation              Analytics
         │                        │
         └───────────┬────────────┘
                     ▼
                 Evidence
                     │
                     ▼
                Conclusion
                     │
                     ▼
            Investment Decision
                     │
                     ▼
              Live Monitoring
                     │
                     ▼
              New Observations


## Practicalities

### I did

    uv add --dev ruff
    uv add --dev mypy
    uv add --dev pytest
    uv add --dev pre-commit

### To run

    uv run ruff check .
    uv run ruff format .

    uv run mypy .

    uv run pytest
    uv run pytest tests/test_login.py

    uv run pre-commit install