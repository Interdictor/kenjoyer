import json


class ConfigProvider():
    def __init__(self):
        self._load()

    def _load(self):
        with open('config.json') as file:
            self.config = json.loads(file.read())


    def provide(self):
        return self.config
        # return { 'auth_token': None }
