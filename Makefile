.PHONY: newday

newday:
	@poetry run cookiecutter .

day=1
test:
	@poetry run python -m unittest discover -s day$(day)

run:
	@poetry run python day$(day)
