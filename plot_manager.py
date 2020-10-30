# library imports
import matplotlib.pyplot as plt

# project imports
from confiremed_model import ConfirmedModel
from country_covid_history import CountryCovidHistory


class PlotManager:
    """
    What this class does
    """

    def __init__(self):
        pass

    @staticmethod
    def plot_fit_model(plot_results: list,
                       country_name: str) -> None:
        """

        :param plot_results:
        :return:
        """
        print("Plot model predictions for: {}".format(country_name))
        for model in plot_results:
            ax = plt.gca()
            ax.plot([i for i in range(len(model.y_data))],
                    model.y_data,
                    "-ok",
                    label="data")
            ax.plot([i for i in range(len(model.y_model))],
                    model.y_model,
                    "-og",
                    label=model.label)
            ax.plot([i for i in range(len(model.y_model), len(model.y_model)+14)],
                    [model.model_function(i, *model.model_parameter) for i in range(len(model.y_model), len(model.y_model)+14)],
                    "--r",
                    label="Model's prediction")
            ax.set_xlabel("Days")
            ax.set_ylabel("Cases")
            ax.set_title("Covid {} confirmed cases with {} models".format(country_name, model.model_name))
            ax.legend()
            plt.savefig("plots/country_plot_{}_model_{}.png".format(model.model_name,
                                                                    country_name))
            #plt.show()
            plt.close()

    @staticmethod
    def plot_data_per_country(data: CountryCovidHistory) -> None:
        """
        :param data: the CountryCovidHistory instance to plot the data
        :return: nothing
        """
        ax = plt.gca()
        ax.plot([i for i in range(len(data.confirmed))],
                data.confirmed,
                "-ob",
                label="confirmed")
        ax.plot([i for i in range(len(data.death))],
                data.death,
                "-sr",
                label="dead")
        ax.plot([i for i in range(len(data.recovered))],
                data.recovered,
                "-*g",
                label="recovered")
        ax.plot([i for i in range(len(data.active))],
                data.active,
                "-^k",
                label="active")
        ax.set_xlabel("Dates from {}".format(data.start_date.strftime("%d.%m.%Y")))
        ax.set_ylabel("Cases")
        ax.set_title("Covid for {}".format(data.name))
        ax.legend()
        plt.savefig("plots/country_plot_{}.png".format(data.name))
        #plt.show()
        plt.close()

    @staticmethod
    def plot_data_per_country_status(data: CountryCovidHistory,
                                     status: str) -> None:
        """
        :param data: the CountryCovidHistory instance to plot the data
        :return: nothing
        """
        ax = plt.gca()
        if status == "confirmed":
            ax.plot([i for i in range(len(data.confirmed))],
                    data.confirmed,
                    "-ob",
                    label="confirmed")
        elif status == "dead":
            ax.plot([i for i in range(len(data.death))],
                    data.death,
                    "-or",
                    label="dead")
        elif status == "recovered":
            ax.plot([i for i in range(len(data.recovered))],
                    data.recovered,
                    "-og",
                    label="recovered")
        elif status == "active":
            ax.plot([i for i in range(len(data.active))],
                    data.active,
                    "-ok",
                    label="active")
        ax.set_xlabel("Dates from {}".format(data.start_date.strftime("%d.%m.%Y")))
        ax.set_ylabel("{} Cases".format(status))
        ax.set_title("Covid for {}".format(data.name))
        ax.legend()
        plt.savefig("plots/country_plot_{}_with_status_{}.png".format(data.name,
                                                                      status))
        #plt.show()
        plt.close()
