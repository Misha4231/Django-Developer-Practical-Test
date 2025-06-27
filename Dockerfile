FROM python:3.11.8 AS base

# install poetry
ENV POETRY_HOME=/opt/poetry
ENV PATH=${POETRY_HOME}/bin:${PATH}

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

RUN apt-get update\
    && apt-get install --no-install-recommends -y curl

RUN curl -sSL https://install.python-poetry.org | python3 - && poetry --version

FROM base AS builder

RUN mkdir /app
WORKDIR /app

# install dependency
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.in-project true
RUN poetry install --only main --no-interaction

FROM base AS runner

WORKDIR /app
COPY --from=builder /app/.venv/ /app/.venv/

COPY . /app

EXPOSE 8000

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]

