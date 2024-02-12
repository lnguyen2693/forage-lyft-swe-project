from battery.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, curr_date, last_service_date):
        self.curr_date = curr_date
        self.last_service_date = last_service_date
    
    def need_service(self):
        need_service_after = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return self.curr_date > need_service_after