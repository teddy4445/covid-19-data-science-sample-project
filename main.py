# library imports
import os
from datetime import datetime

# project imports
from data_study import DataStudy
from data_getter import DataGetter
from plot_manager import PlotManager
from data_preprocess import DataPreprocess
from analysis_manager import AnalysisManager


class Main:
    """
    Managing all the process
    """

    def __init__(self):
        pass

    @staticmethod
    def run():
        """
        Enter point to run the program
        """
        country_names = ["Monaco", "Israel", "Germany"]
        for country in country_names:
            # 1. get data
            data_israel = DataGetter.get_country_data(country_code=country,
                                                      from_date=datetime(year=2020,
                                                                         month=8,
                                                                         day=1),
                                                      to_date=datetime(year=2020,
                                                                       month=10,
                                                                       day=1))
            # 2. data cleaning and formatting
            data_israel = DataPreprocess.fix_country_data(data=data_israel)
            # 3. study data
            DataStudy.investigate(data=data_israel)
            # 4. investigation our questions
            plot_results = AnalysisManager.fit_cases_analysis(data=data_israel)
            # 5. cools graph
            PlotManager.plot_fit_model(plot_results=plot_results,
                                       country_name=data_israel.name)

            print("\n\nFinish with {}\n\n\n\n".format(country))

    @staticmethod
    def build_folders() -> None:
        """
        :return: build the data and plots folders for later use, just to make sure everything works on first run
        """
        try:
            os.makedirs("/data")
        except Exception as error:
            pass
        try:
            os.makedirs("/plots")
        except Exception as error:
            pass


if __name__ == '__main__':
    Main.build_folders()
    Main.run()
