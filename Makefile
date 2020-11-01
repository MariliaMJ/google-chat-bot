.PHONY: help

clean: ## Clean environment
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -f *.log

help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

check:  ## Run static code checks
	@flake8 .
	@isort . --check
	@black --check .

fix-code:  ## Fix some code style
	@isort .
	@black .

outdated: ## Show outdated dependencies
	@pip list --outdated --format=columns

install:  ## Install development dependencies
	@pip install -r requirements.txt
