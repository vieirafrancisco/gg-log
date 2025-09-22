test:
	poetry run pytest

test-cov:
	poetry run pytest --cov

migrate:
	poetry run aerich upgrade

mkm:
	poetry run aerich migrate
