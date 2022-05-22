import pytest
from src.config_provider import ConfigProvider
from src.kenjo_api_client import KenjoApiClient
from test.doubles.requester_double import RequesterDouble


class TestConfigProvider:
    # @pytest.mark.skip()
    def test_it_retrieves_the_configuration(self):
        provider = ConfigProvider()

        result = provider.provide()

        assert result['kenjo_user_id']
        assert result['kenjo_auth_token']
        assert result['start_date']
        assert result['break_time']
        assert result['start_time']
        assert result['end_time']
