# library imports
import os
import json
import requests
from datetime import datetime

# project imports


class DataGetter:
    """
    What this class does
    """

    api_domain = "https://api.covid19api.com"

    def __init__(self):
        pass

    @staticmethod
    def get_all_data() -> dict:
        """
        :return: summery of the data as json
        """
        return DataGetter._save_load_data(path="data/summery_json.json",
                                          url=DataGetter.api_domain + '/summary')

    @staticmethod
    def get_country_data(country_code: str,
                         from_date: datetime,
                         to_date: datetime) -> dict:
        """
        :return: the data of a specific country between two dates
        """
        print("Get Country data for: {}".format(country_code))
        return DataGetter._save_load_data(path="data/country_{}.json".format(country_code),
                                          url="{}/country/{}?from={}T00:00:00Z&to={}T00:00:00Z".format(DataGetter.api_domain,
                                                                                                                        country_code,
                                                                                                                        from_date.strftime("%Y-%m-%d"),
                                                                                                                        to_date.strftime("%Y-%m-%d")))

    @staticmethod
    def _save_load_data(path: str,
                        url: str) -> dict:
        """
        :param path: the path of the file to save \ load data
        :param url: the url to get the data from
        :return: the data from the file or the api call
        """
        if os.path.exists(path):
            with open(path, "r") as data_file:
                answer_json_summery = json.load(data_file)
        else:
            # get data from api
            answer_json_summery = json.loads(requests.get(url=url).text)
            # save it for later use
            with open(path, "w") as data_file:
                json.dump(answer_json_summery, data_file, indent=4, sort_keys=True)
        # return the data
        return answer_json_summery
