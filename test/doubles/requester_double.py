class FakeRequest:
    def __init__(self, request):
        self.request = request
        self.status_code = request['status_code']

    def json(self):
        return self.request['_json']

class RequesterDouble:
    def __init__(self, responses=[], status_code=200):
        self.last_request = None
        self.responses = responses
        self.status_code = status_code

    def post(self, url, **kwargs):
        response = {
            'headers': kwargs.get('headers', {}),
            '_json': self.responses.pop(0),
            'status_code': self.status_code,
        }

        self.last_request = kwargs

        return FakeRequest(response)

    def get(self, url, **kwargs):
        request = {
            'headers': kwargs.get('headers', {}),
            '_json': self.responses.pop(0),
            'status_code': self.status_code,
        }

        self.last_request = request

        return FakeRequest(request)

    def last_request(self):
        return self.last_request
