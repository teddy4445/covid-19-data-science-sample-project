# library imports
from datetime import datetime

# project imports
from country_covid_history import CountryCovidHistory


class DataPreprocess:
    """
    What this class does
    """

    def __init__(self):
        pass

    @staticmethod
    def fix(data: dict) -> list:
        """

        :param data:
        :return:
        """
        pass

    @staticmethod
    def fix_country_data(data: dict) -> CountryCovidHistory:
        """
        :param data:
        :return:
        """
        print("Fix Country data for: {}".format(data[0]['Country']))
        answer = CountryCovidHistory(name=data[0]['Country'],
                                     start_date=datetime.strptime(data[0]['Date'].split("T")[0], '%Y-%m-%d'))
        [answer.add_day(confirmed=day_data["Confirmed"],
                        death=day_data["Deaths"],
                        recovered=day_data["Recovered"],
                        active=day_data["Active"])
         for day_data in data]
        return answer
