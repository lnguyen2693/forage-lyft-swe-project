from battery.battery import Battery
from utils import add_year_to_date


class NubbinBattery(Battery):
    def __init__(self, curr_date, last_service_date):
        self.curr_date = curr_date
        self.last_service_date = last_service_date

    def need_service(self):
        need_service_by = add_year_to_date(self.last_service_date, 4)
        return self.curr_date > need_service_by