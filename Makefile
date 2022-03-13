SHELL=/bin/bash

.PHONY: format
format:
	black .
	isort .
	nbqa black .

.PHONY: shellcheck
shellcheck:
	./.ci/shellcheck.sh

.PHONY: lint
lint: shellcheck
	black --check --diff .
	isort --check .
	diff_lines=$$(nbqa black --check .); \
	if [ $${diff_lines} -gt 0 ]; then \
		echo "Some notebooks would be reformatted by black. Run 'make format' and try again."; \
		exit 1; \
	fi
	flake8 --count .
	nbqa flake8 .
