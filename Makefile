cli:
	docker compose run app

pytest:
	docker compose run app pytest -vv --cov

format_code:
	isort .
	black .