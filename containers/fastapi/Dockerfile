ARG RUNTIME_VERSION="3.11"
FROM python:${RUNTIME_VERSION}
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /application
RUN pip install --upgrade pip && pip install poetry
COPY application/pyproject.toml ./
RUN poetry install
COPY ./containers/fastapi/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh