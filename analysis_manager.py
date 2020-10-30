# library imports
import numpy as np
from scipy.optimize import curve_fit

# project imports
from confiremed_model import ConfirmedModel
from country_covid_history import CountryCovidHistory


class AnalysisManager:
    """
    What this class does
    """

    def __init__(self):
        pass

    @staticmethod
    def fit_cases_analysis(data: CountryCovidHistory) -> list:
        print("Fit Exp model for: {}".format(data.name))
        exp_popt, exp_pcov = curve_fit(exp_func,
                                       [i for i in range(len(data.confirmed))],
                                       data.confirmed)

        print("Fit Linear model for: {}".format(data.name))
        linear_popt, linear_pcov = curve_fit(linear_func,
                                             [i for i in range(len(data.confirmed))],
                                             data.confirmed)
        confirmed_exp_model = [exp_func(i, exp_popt[0], exp_popt[1], exp_popt[2])
                               for i in range(len(data.confirmed))]
        confirmed_linear_model = [linear_func(i, linear_popt[0], linear_popt[1])
                                  for i in range(len(data.confirmed))]
        exp_model = ConfirmedModel(y_data=data.confirmed,
                                   y_model=confirmed_exp_model,
                                   model_function=exp_func,
                                   model_parameter=exp_popt,
                                   fitness=exp_pcov,
                                   model_name="Exp",
                                   label="y = {:.2f} * exp({:.2f}*x) + {:.2f}".format(exp_popt[0], exp_popt[1], exp_popt[2]))
        linear_model = ConfirmedModel(y_data=data.confirmed,
                                      y_model=confirmed_linear_model,
                                      model_function=linear_func,
                                      model_parameter=linear_popt,
                                      fitness=linear_pcov,
                                      model_name="Linear",
                                      label="y = {:.2f} * x + {:.2f}".format(linear_popt[0], linear_popt[1]))
        return [exp_model, linear_model]


def exp_func(x: float,
             a: float,
             b: float,
             c: float) -> float:
    return a * np.exp(x * b) + c


def linear_func(x: float,
                a: float,
                b: float) -> float:
    return a * x + b