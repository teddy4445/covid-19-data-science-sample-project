# library imports
from datetime import datetime, timedelta

# project imports


class CountryCovidHistory:
    """
    What this class does
    """

    def __init__(self,
                 name: str,
                 start_date: datetime):
        self.name = name
        self.start_date = start_date
        self.end_date = start_date
        self.confirmed = []
        self.death = []
        self.recovered = []
        self.active = []

    def add_day(self,
                confirmed: int,
                death: int,
                recovered: int,
                active: int):
        self.confirmed.append(confirmed)
        self.death.append(death)
        self.recovered.append(recovered)
        self.active.append(active)
        # fix the meta data
        self.end_date = self.end_date + timedelta(days=1)

