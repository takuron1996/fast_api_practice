SHELL = /bin/bash
SOURCE_DIR = application
CONTAINER_NAME = fastapi
DOCKER = docker exec $(CONTAINER_NAME)
POETRY_RUN = $(DOCKER) poetry run
DOCS = docs
LINT_RESULT = lint_result.txt

test:
	$(POETRY_RUN) pytest -n auto -ra -p no:cacheprovider --strict-config --strict-markers -vv --diff-symbols --cov --cov-report=html --gherkin-terminal-reporter

up:
	docker-compose up -d

build:
	docker-compose build

down:
	docker-compose down

check:
	@$(POETRY_RUN) black .
	-@$(POETRY_RUN) ruff --fix --show-source --output-format text -o $(LINT_RESULT) .
	@less $(SOURCE_DIR)/$(LINT_RESULT)

install:
	$(DOCKER) poetry install

update:
	$(DOCKER) poetry update

docs:
	@$(POETRY_RUN) pdoc practice -o $(DOCS) -d google

mypy:
	$(POETRY_RUN) mypy --install-types --non-interactive

migration:
	$(POETRY_RUN) alembic revision --autogenerate
