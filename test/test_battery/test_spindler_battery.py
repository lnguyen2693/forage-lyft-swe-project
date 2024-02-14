import unittest
from datetime import datetime

from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_need_service_true(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.need_service())

    def test_need_service_false(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.need_service())