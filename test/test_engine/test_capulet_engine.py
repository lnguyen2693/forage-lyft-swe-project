import unittest


from engine.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_engine_need_service_true(self):
        current_mileage = 40000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.need_service())

    def test_engine_need_service_false(self):
        current_mileage = 20000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.need_service())

