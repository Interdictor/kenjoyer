import json
import pytest
from src.kenjo_api_client import KenjoApiClient
from test.doubles.requester_double import RequesterDouble

from test.samples.response_for_days_off import ResponseForDaysOff

from test.samples.response_for_templates import ResponseForTemplates

from test.doubles.config_provider_double import ConfigProviderDouble


class TestKenjoApiClient:
    def test_it_calls_to_kenjo_with_configured_auth_token(self):
        requester = RequesterDouble([ ResponseForDaysOff.build() ])
        configProvider = ConfigProviderDouble()
        client = KenjoApiClient({ 'requester': requester, 'configProvider': configProvider })


        client.retrieve_time_off_dates()

        last_request = requester.last_request
        assert 'Bearer ey000' in last_request['headers']['Authorization']

    def test_it_retrieves_time_off_dates(self):
        requester = RequesterDouble([ ResponseForDaysOff.build() ])
        client = KenjoApiClient({ 'requester': requester })

        result = client.retrieve_time_off_dates()

        assert result == ['2022-04-14']

    def test_it_retrieves_holidays(self):
        requester = RequesterDouble([ ResponseForTemplates.build() ])
        configProvider = ConfigProviderDouble()
        client = KenjoApiClient({ 'requester': requester, 'configProvider': configProvider })

        result = client.holidays()

        assert result == [
            '2022-04-15',
            '2022-08-15',
            '2022-10-12',
            '2022-11-01',
            '2022-12-06',
            '2022-12-08',
        ]
