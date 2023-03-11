cli:
	docker compose run app

tests:
	docker compose run app pytest -vv --cov

format_code:
	isort .
	black .