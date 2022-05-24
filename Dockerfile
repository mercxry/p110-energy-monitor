FROM python:3.10-alpine3.15 AS base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.8

# Install build tools and poetry
RUN apk add gcc libffi-dev musl-dev \
    && pip install --no-cache-dir "poetry==$POETRY_VERSION"

# Copy python project files
WORKDIR /app
COPY poetry.lock pyproject.toml /app/

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the application
COPY . /app

ENTRYPOINT ["poetry", "run"]
CMD ["python3", "energy_monitor/energy_monitor.py"]
