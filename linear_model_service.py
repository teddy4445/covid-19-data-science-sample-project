# library imports
from datetime import datetime, timedelta

# project imports


class LinearModelService:
    """

    """

    def __init__(self,
                 slope: float,
                 x_intercept: float,
                 end_date: datetime,
                 train_size: int):
        self.slope = slope
        self.x_intercept = x_intercept
        self.end_date = end_date
        self.train_size = train_size

    def predict(self,
                predict_date: datetime) -> float:
        """
        Predicts the number of ____ over time using the trained linear model
        :param predict_date: the date to predict the results
        :return: number of ____ people
        """
        day_to_predict_index = (predict_date - self.end_date).days + self.train_size
        return self.slope * day_to_predict_index + self.x_intercept
