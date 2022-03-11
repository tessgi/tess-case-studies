.PHONY: pytest serve deploy

# Run the unit tests using `pytest`
pytest:
	poetry run pytest --nbmake -s src docs/notebooks/

serve:
	poetry run mkdocs serve

deploy:
		poetry run mkdocs gh-deploy
