.PHONY: test

build:
	docker-compose build

test:
	docker-compose run --rm kenjoyer pytest -vv

t-watch:
	docker-compose run --rm kenjoyer ptw

run:
	docker build . -t kenjoyer && docker run --rm kenjoyer

shell:
	docker-compose run --rm kenjoyer bash
