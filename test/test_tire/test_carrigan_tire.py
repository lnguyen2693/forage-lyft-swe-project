import unittest
from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_need_service_true(self):
        tire_wear = [0.7, 0.92, 0.7, 0.8]
        tire = CarriganTire(tire_wear)
        self.assertTrue(tire.need_service())

    def test_need_service_false(self):
        tire_wear = [0.89] * 4
        tire = CarriganTire(tire_wear)
        self.assertFalse(tire.need_service())