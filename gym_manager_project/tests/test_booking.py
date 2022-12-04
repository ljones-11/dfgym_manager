import unittest
from models.booking import Booking

class TestBooking(unittest.TestCase):
    def setUp(self):
        self.booking1 = Booking("Jack Bauer", "Pilates")

    def test_booking_has_member(self):
        self.assertEqual('Jack Bauer', self.booking1.member)

    def test_booking_has_workout(self):
        self.assertEqual('Pilates', self.booking1.workout)