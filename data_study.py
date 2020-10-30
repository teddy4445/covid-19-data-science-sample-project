# library imports

# project imports
from plot_manager import PlotManager
from country_covid_history import CountryCovidHistory


class DataStudy:
    """
    What this class does
    """

    def __init__(self):
        pass

    @staticmethod
    def investigate(data: CountryCovidHistory) -> None:
        """

        :param data:
        :return:
        """
        print("Print Country raw data in plots for: {}".format(data.name))
        PlotManager.plot_data_per_country(data=data)
        statuses = ["confirmed", "dead", "active", "recovered"]
        for status in statuses:
            PlotManager.plot_data_per_country_status(data=data,
                                                     status=status)