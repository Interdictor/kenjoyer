import pytest
from src.kenjo_api_client import KenjoApiClient
from test.doubles.requester_double import RequesterDouble


class TestKenjoApiClient:
    @pytest.mark.skip()
    def test_it_calls_to_kenjo_with_configured_auth_token(self):
        requester = RequesterDouble()
        client = KenjoApiClient({ 'requester': requester })

        client.retrieve_time_off_dates()

        last_request = requester.last_request
        assert last_request['headers']['Authorization'] == 'Bearer ey000'

    # def test_it_retrieves_time_off_dates(self):
    #     requester = RequesterDouble()
    #     client = KenjoApiClient({ 'requester': requester })

    #     result = client.retrieve_time_off_dates()
