# Backend

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

    # to run:
    uv sync
    uv run uvicorn qtlab.api.main:app --reload --host 0.0.0.0 --port 8080

    # for the db
    uv run alembic revision --autogenerate -m "Create studies and study events"
    uv run alembic upgrade head