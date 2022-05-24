class DaysOffSplit:
    def __init__(self, data):
        self.data = data

    def is_approved(self):
        return self.data['status'].lower() in ['approved', 'processed','inapproval']

    def days_off(self):
        requests = self.data['_splitRequests'][0]
        date = requests['_from'].split('T')

        return [ date[0] ]
