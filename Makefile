.PHONY: test

build:
	docker-compose build

test:
	docker-compose run --rm kenjoyer pytest -vv

twatch:
	docker-compose run --rm kenjoyer ptw

run:
	docker build . -t kenjoyer && docker run --rm kenjoyer

shell:
	docker-compose run --rm kenjoyer bash
