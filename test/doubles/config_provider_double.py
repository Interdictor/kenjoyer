class ConfigProviderDouble:
    def provide(self):
        return {
            "start_date": "2022-04-01",
            "kenjo_user_id": "00aaa00000000000aaa0aa0",
            "kenjo_auth_token": "ey000000000000000000",
            "break_time": "60",
            "start_time": "480",
            "end_time": "1020",
            "template_key": "spain",
            "_": "all the below keys are just comments. There is no need to edit them",
            "__": "remember to edit config.json and not config_example.json file",
            "_start_date": "ensure you are using the given date format, %Y-%m-%d",
            "_kenjo_auth_token": "do not include 'Bearer' prefix",
            "_break_time": "this is the amount of minutes you take as break during your working day",
            "_start_and_end_time": "the minutes since 00:00 when you start/end to work.",
            "_addendum": "480 is the same that 08:00 and 1020, 17:00. Feel free to edit them."
        }
