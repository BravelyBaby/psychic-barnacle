.PHONY: help build run test

help:
	@echo "Makefile targets:"
	@echo "  build  - build a Docker image when a Dockerfile is added"
	@echo "  run    - run the Docker image"
	@echo "  test   - run tests (replace with your language/test runner)"

build:
	@if [ -f Dockerfile ]; then \
		docker build -t psychic-barnacle .; \
	else \
		echo "No Dockerfile found. Add one to use 'make build'"; \
	fi

run:
	@if [ -f Dockerfile ]; then \
		docker run --rm -it psychic-barnacle; \
	else \
		echo "No Dockerfile found. Add one to use 'make run'"; \
	fi

test:
	@echo "No tests configured. Add your language test runner here (e.g., npm test or pytest)"
