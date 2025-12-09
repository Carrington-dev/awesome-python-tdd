import unittest
from main import ReservationSystem


class TestReservation(unittest.TestCase):
    def setUp(self):
        self.reservation_system = ReservationSystem(departure = "Pretoria", destination = "Limpopo, Polokwane")

    def tearDown(self):
        self.reservation_system = None

    def test_reservation_has_destination(self):
        self.assertNotEqual(None, self.reservation_system.destination)

    def test_reservation_has_destination(self):
        self.assertNotEqual(None, self.reservation_system.departure)

        