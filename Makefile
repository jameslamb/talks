SHELL=/bin/bash

.PHONY: format
format:
	black .
	nbqa black . --nbqa-mutate

.PHONY: lint
lint:
	black --check --diff .
	diff_lines=$$(nbqa black --nbqa-diff . | wc -l); \
	if [ $${diff_lines} -gt 0 ]; then \
		echo "Some notebooks would be reformatted by black. Run 'make format' and try again."; \
		exit 1; \
	fi
	flake8 --count .
	nbqa flake8 .
