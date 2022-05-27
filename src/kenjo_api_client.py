from functools import reduce
from src.iso_pattern import IsoPattern
from src.days_off_split import DaysOffSplit
from src.config_provider import ConfigProvider
from src.requester import Requester
from datetime import datetime


class KenjoApiClient:
    DOMAIN = 'https://api.kenjo.io'
    TIMESTAMP_SUFFIX = 'T00:00:00.000Z'

    def __init__(self, dependencies={}):
        configProvider = dependencies.get('configProvider') or ConfigProvider()

        self.config = configProvider.provide()
        self.requester = dependencies.get('requester') or Requester()


    def retrieve_punched_dates(self):
        url = self.DOMAIN + '/user-attendance-db/find'
        start_timestamp = self.config['start_date'] + self.TIMESTAMP_SUFFIX
        now_timestamp = datetime.now().isoformat() + 'Z'

        payload = {
            "_userId": self.config['kenjo_user_id'],
            "date": { "$gte": start_timestamp, "$lte" : now_timestamp },
            "_deleted": False,
        }
        response = self.requester.post(url, headers=self._build_headers(), json=payload)
        return [recorded_punch['date'].split('T')[0] for recorded_punch in response.json()]

    def punch(self, timestamp):
        url = self.DOMAIN + '/user-attendance-db'


        payload = {
            "_userId": self.config['kenjo_user_id'],
            "ownerId": self.config['kenjo_user_id'],
            "date": timestamp + self.TIMESTAMP_SUFFIX,
            "startTime": self.config['start_time'],
            "endTime": self.config['end_time'],
            "breakTime": self.config['break_time'],
            "_changesTracking":[],
            "_deleted": False,
            "_approved": False
        }

        response = self.requester.post(url, headers=self._build_headers(), json=payload)
        if response.status_code > 400:
            print(response.status_code)
            raise RuntimeError(f'Unable to punch. Kenjo API status code: {response.status_code}')

    def retrieve_time_off_dates(self):
        payload = { "_userId": self.config['kenjo_user_id'] }
        request = self.requester.post(
            self.DOMAIN + '/user-time-off-request/find',
            headers=self._build_headers(),
            json=payload,
        )

        if request.status_code > 400:
            raise RuntimeError(f'[ERROR] Unable to retrieve time off dates. Kenjo API response code: {request.status_code}. Is the auth token properly setted and updated?')

        response_payload = request.json()
        holidays = self.holidays()

        splits = [ DaysOffSplit(split_data, holidays) for split_data in response_payload ]
        processed_splits = [ split for split in splits if split.is_relevant() ]
        days_off = reduce(lambda accumulator, split: accumulator + split.days_off(), processed_splits, [])

        return { 'days_off': days_off, 'holidays': holidays }

    def holidays(self):
        request = self.requester.get(
            self.DOMAIN + '/calendar-template-db/templates',
            headers=self._build_headers(),
        )

        country = self.config['template_key']
        response_body = request.json()

        relevant_template = [holiday_template for holiday_template in response_body if holiday_template['templateKey'] == country]
        holidays = [holiday['holidayDate'] for holiday in relevant_template[0]['holidays']]
        return [holiday for holiday in holidays if datetime.strptime(holiday, IsoPattern.DATE.value) >= datetime.strptime(self.config['start_date'], IsoPattern.DATE.value)]

    def _build_headers(self):
        return {
            'Authorization': 'Bearer ' + self.config['kenjo_auth_token'],
            'Origin': 'https://app.kenjo.io',
            'Content-type': 'application/json',
        }
