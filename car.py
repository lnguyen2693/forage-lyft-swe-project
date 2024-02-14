from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.battery.need_service() or self.engine.need_service()


# from abc import ABC, abstractmethod


# class Car(ABC):
#     def __init__(self, last_service_date):
#         self.last_service_date = last_service_date

#     @abstractmethod
#     def needs_service(self):
#         pass
