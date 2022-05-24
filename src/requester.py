import requests


class Requester:
    def post(self, url, **kwargs):
        return requests.post(url, **kwargs)

    def get(self, url, **kwargs):
       return requests.get(url, **kwargs)
