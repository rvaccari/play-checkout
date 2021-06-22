pre-install:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

install:
	poetry install

configure:
	poetry run python contrib/env_gen.py

run:
	poetry run python manage.py runserver

format:
	poetry run black backend contrib

test:
	poetry run pytest -ra --disable-warnings --color=yes $(ARGS)

test-parallel:
	$(eval TEST_WORKERS ?= 4)
	$(eval ARGS ?= -n $(TEST_WORKERS) --dist=loadfile $(EXTRA_ARGS))
	make test ARGS="$(ARGS)"

ci:
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -f .coverage
	make test ARGS="--cov=backend --cov-fail-under=70 --mypy --black $(ARGS)"

ci-parallel:
	$(eval TEST_WORKERS ?= 4)
	$(eval ARGS ?= -n $(TEST_WORKERS) --dist=loadfile $(EXTRA_ARGS))
	make ci ARGS="$(ARGS)"

docker-build:
	docker build .

docker-up:
	docker-compose up -d

docker-stop:
	docker-compose stop
