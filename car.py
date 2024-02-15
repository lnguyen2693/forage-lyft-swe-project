from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self):
        return self.battery.need_service() or self.engine.need_service() or self.tire.need_service()

