# KENJOYER

## REQUIREMENTS
* python 3

## SETUP
  * Duplicate the file config_example.json, rename it to "config.json" and fill it with your custom configuration. You will need your kenjo user id and auth token, You can retrieve them user chrome/firefox dev tools (or ask a developer for help)

## REGULAR USER COMMANDS
  * `pip install -r requirements.txt`
  * `python3 src/main.py`

## DEV REQUIREMENTS
  * Docker 20.10.16 or superior
  * docker-compose 1.29.2 or superior
  * GNU Make

Dev commands are listed in the Makefile. Launch `make build` to initialize the project
