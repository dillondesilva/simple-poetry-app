FROM python:3.7-alpine

COPY app/ app/
COPY tests/ tests/

COPY entrypoint.sh entrypoint.sh

ENTRYPOINT ["/bin/sh", "entrypoint.sh"]