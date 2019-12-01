.PHONY: test

test: .venv3/bin/pytest .venv3/bin/mypy
	.venv3/bin/mypy --strict app
	.venv3/bin/pytest tests -v --capture=no --cov app --cov-fail-under 100  --cov-report term-missing

.venv3/bin/pip:
	python3 -m venv --prompt=k2 .venv3

.venv3/bin/pytest: .venv3/bin/pip
	.venv3/bin/pip install pytest-cov

.venv3/bin/mypy: .venv3/bin/pip
	.venv3/bin/pip install mypy