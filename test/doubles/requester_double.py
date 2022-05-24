class FakeRequest:
    def __init__(self, request):
        self.request = request

    def json(self):
        return self.request['_json']

class RequesterDouble:
    def __init__(self, responses=[]):
        self.last_request = None
        self.responses = responses

    def post(self, url, **kwargs):
        request = {
            'headers': kwargs.get('headers', {}),
            '_json': self.responses.pop(),
        }

        self.last_request = request

        return FakeRequest(request)

    def get(self, url, **kwargs):
        request = {
            'headers': kwargs.get('headers', {}),
            '_json': self.responses.pop(),
        }

        self.last_request = request

        return FakeRequest(request)

    def last_request(self):
        return self.last_request
