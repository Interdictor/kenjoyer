from functools import reduce
from src.IsoPattern import IsoPattern
from src.days_off_split import DaysOffSplit
from src.config_provider import ConfigProvider
from src.requester import Requester
from datetime import datetime



class KenjoApiClient:
    DOMAIN = 'https://api.kenjo.io'
    def __init__(self, dependencies={}):
        configProvider = dependencies.get('configProvider') or ConfigProvider()

        self.config = configProvider.provide()
        self.requester = dependencies.get('requester', Requester())


    # TIMESTAMP_SUFFIX = 'T00:00:00.000Z'
    # @classmethod
    # def retrieve_punched_dates(cls):
    #     config = ConfigProvider.provide()
    #     url = cls.DOMAIN + '/user-attendance-db/find'

    #     timestamp_suffix = 'T00:00:00.000Z'
    #     start_timestamp = config['start_date'] + timestamp_suffix
    #     now_timestamp = datetime.now().isoformat() + 'Z'


    #     payload = {
    #         "_userId":"lol",
    #         "date": { "$gte": start_timestamp, "$lte" : now_timestamp },
    #         "_deleted": False,
    #     }

    #     response = requests.post(url, headers=cls.headers(), json=payload)
    #     return [punch['date'].split('T')[0] for punch in response.json()]

    # @classmethod
    # def punch(cls, timestamp):
    #     url = cls.DOMAIN + '/user-attendance-db'

    #     payload = {
    #         "_userId":"lol",
    #         "ownerId":"lol",
    #         "date":timestamp + cls.TIMESTAMP_SUFFIX,
    #         "startTime":480,
    #         "endTime":1020,
    #         "breakTime":60,
    #         "_changesTracking":[],
    #         "_deleted": False,
    #         "_approved": False
    #     }

    #     response = requests.post(url, headers=cls.headers(), json=payload)
    #     if response.status_code not in [200, 201]:
    #         print(response.status_code)
    #         raise RuntimeError()


    def retrieve_time_off_dates(self):
        payload = { "_userId": self.config['kenjo_user_id'] }

        request = self.requester.post(
            self.DOMAIN + '/user-time-off-request/find',
            headers=self._build_headers(),
            json=payload,
        )

        response_payload = request.json()

        splits = [ DaysOffSplit(split_data) for split_data in response_payload ]
        processed_splits = [ split for split in splits if split.is_approved() ]
        days_off = reduce(lambda accumulator, split: split.days_off() + accumulator, processed_splits, [])

        return days_off

    def holidays(self):
        request = self.requester.get(
            self.DOMAIN + '/calendar-template-db/templates',
            headers=self._build_headers(),
        )

        country = 'spain'
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
