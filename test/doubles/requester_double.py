class RequesterDouble:
    def __init__(self):
        self.last_request = None

    def post(self, url, **kwargs):
        request = {
            'headers': kwargs.get('headers', {}),
            'json': kwargs.get('json', {}),
        }

        self.last_request = request

    def last_request(self):
        return self.last_request
