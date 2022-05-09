.PHONY: test

build:
	docker-compose build

test:
	docker-compose run --rm kenjoyer pytest

run:
	docker build . -t kenjoyer && docker run --rm kenjoyer
