.PHONY: test

build:
	docker-compose build

test:
	docker-compose run --rm kenjoyer pytest -vv

twatch:
	docker-compose run --rm kenjoyer ptw

run:
	docker-compose run --rm kenjoyer

shell:
	docker-compose run --rm kenjoyer bash
