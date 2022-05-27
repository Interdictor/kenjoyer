from src.days_off_split import DaysOffSplit

class TestDaysOffSplit:
    def test_it_calculates_the_days_off_properly(self):
        data = { '_splitRequests': [ { "_from": "2022-05-25T00:00:00.000Z" ,"_workingDays": 5 } ] }
        holidays = []
        split = DaysOffSplit(data, holidays)

        result = split.days_off()

        assert result == [
            '2022-05-25',
            '2022-05-26',
            '2022-05-27',
            '2022-05-30',
            '2022-05-31',
        ]

    def test_it_calculates_the_days_off_taking_in_account_holidays(self):
        data = { '_splitRequests': [ { "_from": "2022-05-25T00:00:00.000Z" ,"_workingDays": 5 } ] }
        holidays = ['2022-05-27']
        split = DaysOffSplit(data, holidays)

        result = split.days_off()

        assert result == [
            '2022-05-25',
            '2022-05-26',
            '2022-05-30',
            '2022-05-31',
            '2022-06-01',
        ]

    def test_it_calculates_the_days_off_of_many_splits(self):
        data = { '_splitRequests': [
                { "_from": "2022-05-25T00:00:00.000Z" ,"_workingDays": 5 },
                { "_from": "2022-06-25T00:00:00.000Z" ,"_workingDays": 5 },
            ]
        }
        holidays = ['2022-05-27']
        split = DaysOffSplit(data, holidays)

        result = split.days_off()

        assert len(result) == 10
        assert result == [
            '2022-05-25',
            '2022-05-26',
            '2022-05-30',
            '2022-05-31',
            '2022-06-01',
            '2022-06-27',
            '2022-06-28',
            '2022-06-29',
            '2022-06-30',
            '2022-07-01',
        ]
