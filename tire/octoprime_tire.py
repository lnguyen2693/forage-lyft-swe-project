from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    
    def need_service(self):
        return sum(self.tire_wear) >= 3
        
# should be serviced only when the sum of all values 
# in the tire wear array is greater than or equal to 3.