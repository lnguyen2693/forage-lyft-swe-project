import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_need_service_true(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.need_service())

    def test_need_service_false(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.need_service())
