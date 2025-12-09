import unittest
from booking import Booking, ReversationSystem, logger

class TestBooking(unittest.TestCase):
    def setUp(self):
        self.booking = Booking()

    def tearDown(self):
        self.booking = None
    
    def test_booking_has_required_arguments(self):
        self.assertNotEqual(self.booking.full_name, None)
        self.assertNotEqual(self.booking.room_number, None)
        self.assertNotEqual(self.booking.check_in_date, None)
        self.assertNotEqual(self.booking.check_out_date, None)

    def test_booking_reference_automatically_generated(self):
        self.assertNotEqual(None, self.booking.booking_reference)

    def test_booking_check_out_date_is_after_check_in_date(self):
        self.assertGreater(self.booking.check_out_date, self.booking.check_in_date)

class TestReservationSystem(unittest.TestCase):
    def setUp(self):
        self.reservation_system =  ReversationSystem()
    
    def tearDown(self):
        self.reservation_system = None

    def test_if_reservation_system_has_user_lists(self):
        self.assertNotEqual([], self.reservation_system.user_list)

    def test_if_reservation_system_highlights_bookings_availability(self):
        "Check if reservation system highlights if the hotel is full booked or not"
        self.assertIsNotNone(self.reservation_system.TOTAL_BOOKINGS_PER_DAY)

    def test_if_reservation_system_can_pick_valid_and_invalid_users(self):
        fake_user_id = "9270300785088"
        with self.assertRaises(Exception):
            self.reservation_system.book_for_user_by_id(fake_user_id, 2)

    def test_if_user_not_booked_already(self):
        real_user_id = '6292344283081'
        self.reservation_system.book_for_user_by_id(real_user_id)
        with self.assertRaises(Exception):
            self.reservation_system.book_for_user_by_id(real_user_id)


    def test_if_one_book_successfully(self):
        real_user_id = '6292344283081'
        expected_results = "booking_reference" in self.reservation_system.book_for_user_by_id(real_user_id)
        self.assertEqual(expected_results, True)
    


    