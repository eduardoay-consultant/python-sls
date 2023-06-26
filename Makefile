# Analyze the given Python modules and compute Cyclomatic Complexity
cc_json = "$(shell poetry run radon cc --min B src --json)"

# Analyze the given Python modules and compute the Maintainability Index
mi_json = "$(shell poetry run radon mi --min B src --json)"

# Get list of files to analyze
files = `find ./config ./lambda_funcs ./src ./tests -name "*.py"`
files_tests = `find ./tests -name "*.py"`

help: ## Display this help screen.
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

lint: ## Run Pylint checks on the project.
	@poetry run pylint $(files)

format: ## Run Black formatter on the project.
	@poetry run black $(files)

test: ## Run tests on the project.
	@poetry run pytest $(files_tests)

complexity: ## Run radon complexity checks for maintainability status.
	@echo "Complexity check..."

ifneq ($(cc_json), "{}")
	@echo
	@echo "Complexity issues"
	@echo "-----------------"
	@echo $(cc_json)
endif

ifneq ($(mi_json), "{}")
	@echo
	@echo "Maintainability issues"
	@echo "----------------------"
	@echo $(mi_json)
endif

ifneq ($(cc_json), "{}")
	@echo
	exit 1
else
ifneq ($(mi_json), "{}")
	@echo
	exit 1
endif
endif

	@echo "OK"
.PHONY: complexity

install_hooks: ## Install pre-commit hooks.
	@pre-commit install && pre-commit install --hook-type commit-msg
