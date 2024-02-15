from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def need_service(self):
        values = list(filter(lambda x : x >= 0.9, self.tire_wear))
        return len(values) > 0

# should be serviced only when one or more of the values 
# in the tire wear array is greater than or equal to 0.9.