from tire.octoprime_tire import OctoprimeTire
import unittest


class TestOctoprimeTire(unittest.TestCase):
    def test_need_service_true(self):
        tire_wear = [0.7, 0.9, 0.7, 0.8]
        tire = OctoprimeTire(tire_wear)
        self.assertTrue(tire.need_service())