import json


class ConfigProvider():
    def __init__(self):
        self._load()

    def _load(self):
        with open('config.json') as file:
            config = json.loads(file.read())

        print(config)
        self.config = config

    def provide(self):
        return self.config
        # return { 'auth_token': None }
