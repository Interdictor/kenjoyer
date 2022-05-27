from datetime import datetime, timedelta
from src.iso_pattern import IsoPattern
from src.weekday import Weekday


class DaysOffSplit:
    def __init__(self, data, holidays):
        self.data = data
        self.holidays = holidays

    def is_relevant(self):
        return self.data['status'].lower() in ['approved', 'processed','inapproval', 'pending']

    def days_off(self):
        # return if not self.is_relevant

        requests = self.data['_splitRequests']
        requests = map(lambda request: self._calculateDaysOff(request), requests)
        return [item for sublist in requests for item in sublist]

    def _calculateDaysOff(self, request):
        beginning_datestamp = request['_from'].split('T')[0]
        # return [holiday for holiday in holidays if datetime.strptime(holiday, IsoPattern.DATE.value) >= datetime.strptime(self.config['start_date'], IsoPattern.DATE.value)]
        beginning_date = datetime.strptime(beginning_datestamp, IsoPattern.DATE.value)

        remaining_working_days = request['_workingDays']
        days_off = []

        iteration_date = beginning_date
        while remaining_working_days > 0:
            if(iteration_date.weekday() in [Weekday.SATURDAY.value, Weekday.SUNDAY.value]):
                iteration_date += timedelta(days=1)
                continue

            if(iteration_date.strftime(IsoPattern.DATE.value) in self.holidays):
                iteration_date += timedelta(days=1)
                continue

            datestamp = iteration_date.strftime(IsoPattern.DATE.value)
            days_off.append(datestamp)
            remaining_working_days = remaining_working_days - 1
            iteration_date += timedelta(days=1)

        return days_off
