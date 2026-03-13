# Variables
APP_NAME := toxicity-predicator
DOCKER_IMG := $(APP_NAME)

# Docker
build:
	docker build -t $(DOCKER_IMG) .

run:
	docker run --name $(DOCKER_IMG) --rm -v $(PWD):/app $(DOCKER_IMG)


# Rebuild only on change in dependencies
rebuild:
	docker build --no-cache -t $(DOCKER_IMG) .