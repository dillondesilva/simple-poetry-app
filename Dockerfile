FROM python:3.7-alpine

COPY app/ project/app/
COPY tests/ project/tests/
COPY poetry.lock project/poetry.lock
COPY pyproject.toml project/pyproject.toml

COPY entrypoint.sh entrypoint.sh

ENTRYPOINT ["/bin/sh", "entrypoint.sh"]