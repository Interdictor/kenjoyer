
from datetime import datetime, timedelta, time
from src.iso_pattern import IsoPattern
from src.config_provider import ConfigProvider
from src.kenjo_api_client import KenjoApiClient

client = KenjoApiClient()
configProvider = ConfigProvider()

config = configProvider.provide()

already_punched_timestamps = client.retrieve_punched_dates()
time_off = client.retrieve_time_off_dates()
day_off_timestamps = time_off['days_off']
holidays = time_off['holidays']

start_date = datetime.strptime(config['start_date'], IsoPattern.DATE.value)

def generate_date(start_date):
    today = datetime.combine(datetime.utcnow(), time.min)
    current_date = start_date
    while current_date < today:
        yield current_date
        current_date += timedelta(days=1)


for day in generate_date(start_date):
    current_timestamp = day.strftime(IsoPattern.DATE.value)

    if current_timestamp in holidays:
        print(f'[SKIP] {current_timestamp} - Is a holiday')
        continue

    if current_timestamp in day_off_timestamps:
        print(f'[SKIP] {current_timestamp} - Is a day off')
        continue

    if current_timestamp in already_punched_timestamps:
        print(f'[SKIP] {current_timestamp} - Already punched')
        continue

    client.punch(current_timestamp)
    print(f'[SUCCESS] {current_timestamp} - Punched')
