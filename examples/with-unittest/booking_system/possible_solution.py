# booking_system.py
from datetime import datetime, timedelta
import uuid


class BookingException(Exception):
    """Base exception for booking errors"""
    pass


class RoomNotAvailableException(BookingException):
    """Raised when room is not available for requested dates"""
    pass


class InvalidBookingException(BookingException):
    """Raised when booking data is invalid"""
    pass


class Booking:
    """Represents a hotel room booking"""
    
    def __init__(self, guest_name, room_number, check_in, check_out, num_guests=1):
        if not guest_name:
            raise InvalidBookingException("Guest name is required")
        if check_out <= check_in:
            raise InvalidBookingException("Check-out date must be after check-in date")
        if num_guests < 1:
            raise InvalidBookingException("Number of guests must be at least 1")
            
        self.reference_id = self._generate_reference()
        self.guest_name = guest_name
        self.room_number = room_number
        self.check_in = check_in
        self.check_out = check_out
        self.num_guests = num_guests
        self.is_cancelled = False
        self.created_at = datetime.now()
    
    def _generate_reference(self):
        """Generate unique booking reference"""
        return f"BK{uuid.uuid4().hex[:8].upper()}"
    
    def get_nights(self):
        """Calculate number of nights"""
        return (self.check_out - check_in).days
    
    def __repr__(self):
        return f"Booking({self.reference_id}, {self.guest_name}, Room {self.room_number})"


class Room:
    """Represents a hotel room with capacity and pricing"""
    
    ROOM_TYPES = {
        'standard': {'capacity': 2, 'base_rate': 100},
        'deluxe': {'capacity': 3, 'base_rate': 150},
        'suite': {'capacity': 4, 'base_rate': 200}
    }
    
    def __init__(self, room_number, room_type='standard'):
        if room_type not in self.ROOM_TYPES:
            raise ValueError(f"Invalid room type. Must be one of {list(self.ROOM_TYPES.keys())}")
        
        self.room_number = room_number
        self.room_type = room_type
        self.capacity = self.ROOM_TYPES[room_type]['capacity']
        self.base_rate = self.ROOM_TYPES[room_type]['base_rate']


class BookingSystem:
    """Main booking system to manage hotel reservations"""
    
    EXTRA_GUEST_FEE = 25
    WEEKEND_SURCHARGE_RATE = 0.20
    LONG_STAY_DISCOUNT_7 = 0.10
    LONG_STAY_DISCOUNT_14 = 0.15
    
    def __init__(self):
        self.bookings = []
        self.rooms = {}
    
    def add_room(self, room_number, room_type='standard'):
        """Add a room to the system"""
        self.rooms[room_number] = Room(room_number, room_type)
    
    def book_room(self, guest_name, room_number, check_in, check_out, num_guests=1):
        """
        Create a new booking for a room
        
        Args:
            guest_name: Name of the guest
            room_number: Room number to book
            check_in: Check-in date
            check_out: Check-out date
            num_guests: Number of guests (default 1)
            
        Returns:
            Booking object
            
        Raises:
            RoomNotAvailableException: If room is not available
            InvalidBookingException: If booking data is invalid
        """
        # Check if room exists
        if room_number not in self.rooms:
            raise InvalidBookingException(f"Room {room_number} does not exist")
        
        # Check capacity
        room = self.rooms[room_number]
        if num_guests > room.capacity:
            raise InvalidBookingException(
                f"Room {room_number} has capacity {room.capacity}, cannot book for {num_guests} guests"
            )
        
        # Check availability
        if not self.is_room_available(room_number, check_in, check_out):
            raise RoomNotAvailableException(
                f"Room {room_number} is not available for the requested dates"
            )
        
        # Create booking
        booking = Booking(guest_name, room_number, check_in, check_out, num_guests)
        self.bookings.append(booking)
        
        return booking
    
    def is_room_available(self, room_number, check_in, check_out):
        """
        Check if a room is available for given dates
        
        Args:
            room_number: Room number to check
            check_in: Desired check-in date
            check_out: Desired check-out date
            
        Returns:
            True if available, False otherwise
        """
        for booking in self.bookings:
            if booking.room_number == room_number and not booking.is_cancelled:
                # Check for date overlap
                if self._dates_overlap(
                    booking.check_in, booking.check_out,
                    check_in, check_out
                ):
                    return False
        return True
    
    def _dates_overlap(self, start1, end1, start2, end2):
        """Check if two date ranges overlap"""
        # Ranges overlap if one starts before the other ends
        return start1 < end2 and start2 < end1
    
    def cancel_booking(self, reference_id):
        """
        Cancel a booking by reference ID
        
        Args:
            reference_id: Booking reference ID
            
        Returns:
            Cancelled booking object
            
        Raises:
            InvalidBookingException: If booking not found or already cancelled
        """
        booking = self.get_booking_by_reference(reference_id)
        
        if booking.is_cancelled:
            raise InvalidBookingException(f"Booking {reference_id} is already cancelled")
        
        booking.is_cancelled = True
        return booking
    
    def get_booking_by_reference(self, reference_id):
        """Get booking by reference ID"""
        for booking in self.bookings:
            if booking.reference_id == reference_id:
                return booking
        raise InvalidBookingException(f"Booking {reference_id} not found")
    
    def modify_booking_dates(self, reference_id, new_check_in, new_check_out):
        """
        Modify the dates of an existing booking
        
        Args:
            reference_id: Booking reference ID
            new_check_in: New check-in date
            new_check_out: New check-out date
            
        Returns:
            Modified booking object
            
        Raises:
            InvalidBookingException: If dates invalid or booking not found
            RoomNotAvailableException: If room not available for new dates
        """
        booking = self.get_booking_by_reference(reference_id)
        
        if booking.is_cancelled:
            raise InvalidBookingException("Cannot modify cancelled booking")
        
        if new_check_out <= new_check_in:
            raise InvalidBookingException("Check-out must be after check-in")
        
        # Temporarily mark booking as cancelled to check availability
        original_check_in = booking.check_in
        original_check_out = booking.check_out
        booking.is_cancelled = True
        
        try:
            if not self.is_room_available(booking.room_number, new_check_in, new_check_out):
                booking.is_cancelled = False
                raise RoomNotAvailableException(
                    f"Room {booking.room_number} not available for new dates"
                )
            
            # Update dates
            booking.check_in = new_check_in
            booking.check_out = new_check_out
            booking.is_cancelled = False
            
            return booking
            
        except Exception:
            # Restore original state if something goes wrong
            booking.check_in = original_check_in
            booking.check_out = original_check_out
            booking.is_cancelled = False
            raise
    
    def calculate_cost(self, booking):
        """
        Calculate total cost for a booking
        
        Args:
            booking: Booking object or reference ID
            
        Returns:
            Total cost as float
        """
        if isinstance(booking, str):
            booking = self.get_booking_by_reference(booking)
        
        room = self.rooms[booking.room_number]
        nights = (booking.check_out - booking.check_in).days
        
        if nights <= 0:
            raise InvalidBookingException("Invalid booking duration")
        
        # Base cost
        total = room.base_rate * nights
        
        # Extra guest fee (per night for guests above 2)
        if booking.num_guests > 2:
            extra_guests = booking.num_guests - 2
            total += extra_guests * self.EXTRA_GUEST_FEE * nights
        
        # Weekend surcharge
        weekend_nights = self._count_weekend_nights(booking.check_in, booking.check_out)
        weekend_surcharge = room.base_rate * weekend_nights * self.WEEKEND_SURCHARGE_RATE
        total += weekend_surcharge
        
        # Long stay discount
        if nights >= 14:
            total *= (1 - self.LONG_STAY_DISCOUNT_14)
        elif nights >= 7:
            total *= (1 - self.LONG_STAY_DISCOUNT_7)
        
        return round(total, 2)
    
    def _count_weekend_nights(self, check_in, check_out):
        """Count Friday and Saturday nights in date range"""
        count = 0
        current = check_in
        while current < check_out:
            # 4 = Friday, 5 = Saturday in weekday()
            if current.weekday() in [4, 5]:
                count += 1
            current += timedelta(days=1)
        return count
    
    def calculate_refund(self, reference_id, cancellation_date=None):
        """
        Calculate refund amount based on cancellation policy
        
        Policy:
        - Full refund if cancelled 7+ days before check-in
        - 50% refund if cancelled 3-6 days before check-in
        - No refund if cancelled within 2 days of check-in
        
        Args:
            reference_id: Booking reference ID
            cancellation_date: Date of cancellation (defaults to now)
            
        Returns:
            Refund amount as float
        """
        booking = self.get_booking_by_reference(reference_id)
        
        if cancellation_date is None:
            cancellation_date = datetime.now().date()
        
        days_until_checkin = (booking.check_in - cancellation_date).days
        total_cost = self.calculate_cost(booking)
        
        if days_until_checkin >= 7:
            return total_cost  # Full refund
        elif days_until_checkin >= 3:
            return round(total_cost * 0.5, 2)  # 50% refund
        else:
            return 0.0  # No refund
    
    def get_bookings_by_guest(self, guest_name):
        """Get all bookings for a specific guest"""
        return [b for b in self.bookings if b.guest_name == guest_name and not b.is_cancelled]
    
    def get_bookings_by_room(self, room_number):
        """Get all bookings for a specific room"""
        return [b for b in self.bookings if b.room_number == room_number and not b.is_cancelled]
    
    def get_upcoming_bookings(self, as_of_date=None):
        """Get all upcoming bookings (check-in date in future)"""
        if as_of_date is None:
            as_of_date = datetime.now().date()
        
        return [
            b for b in self.bookings 
            if b.check_in >= as_of_date and not b.is_cancelled
        ]
    
    def get_active_bookings(self, as_of_date=None):
        """Get all currently active bookings (checked in but not checked out)"""
        if as_of_date is None:
            as_of_date = datetime.now().date()
        
        return [
            b for b in self.bookings
            if b.check_in <= as_of_date < b.check_out and not b.is_cancelled
        ]


# ============================================================================
# UNIT TESTS
# ============================================================================

import unittest


class TestBooking(unittest.TestCase):
    """Test the Booking class"""
    
    def test_create_booking_with_valid_data(self):
        check_in = datetime(2024, 12, 10).date()
        check_out = datetime(2024, 12, 15).date()
        
        booking = Booking("John Doe", 101, check_in, check_out)
        
        self.assertEqual(booking.guest_name, "John Doe")
        self.assertEqual(booking.room_number, 101)
        self.assertEqual(booking.check_in, check_in)
        self.assertEqual(booking.check_out, check_out)
        self.assertIsNotNone(booking.reference_id)
        self.assertTrue(booking.reference_id.startswith("BK"))
    
    def test_booking_reference_is_unique(self):
        check_in = datetime(2024, 12, 10).date()
        check_out = datetime(2024, 12, 15).date()
        
        booking1 = Booking("John Doe", 101, check_in, check_out)
        booking2 = Booking("Jane Smith", 102, check_in, check_out)
        
        self.assertNotEqual(booking1.reference_id, booking2.reference_id)
    
    def test_checkout_must_be_after_checkin(self):
        check_in = datetime(2024, 12, 15).date()
        check_out = datetime(2024, 12, 10).date()
        
        with self.assertRaises(InvalidBookingException):
            Booking("John Doe", 101, check_in, check_out)
    
    def test_guest_name_required(self):
        check_in = datetime(2024, 12, 10).date()
        check_out = datetime(2024, 12, 15).date()
        
        with self.assertRaises(InvalidBookingException):
            Booking("", 101, check_in, check_out)


class TestRoomAvailability(unittest.TestCase):
    """Test room availability checking"""
    
    def setUp(self):
        self.system = BookingSystem()
        self.system.add_room(101)
    
    def test_room_available_when_no_bookings(self):
        check_in = datetime(2024, 12, 10).date()
        check_out = datetime(2024, 12, 15).date()
        
        available = self.system.is_room_available(101, check_in, check_out)
        
        self.assertTrue(available)
    
    def test_room_unavailable_with_exact_overlap(self):
        check_in = datetime(2024, 12, 10).date()
        check_out = datetime(2024, 12, 15).date()
        
        self.system.book_room("John Doe", 101, check_in, check_out)
        
        available = self.system.is_room_available(101, check_in, check_out)
        self.assertFalse(available)
    
    def test_room_unavailable_with_partial_overlap(self):
        check_in1 = datetime(2024, 12, 10).date()
        check_out1 = datetime(2024, 12, 15).date()
        
        self.system.book_room("John Doe", 101, check_in1, check_out1)
        
        # New booking overlaps at the end
        check_in2 = datetime(2024, 12, 12).date()
        check_out2 = datetime(2024, 12, 17).date()
        
        available = self.system.is_room_available(101, check_in2, check_out2)
        self.assertFalse(available)
    
    def test_room_available_for_different_dates(self):
        check_in1 = datetime(2024, 12, 10).date()
        check_out1 = datetime(2024, 12, 15).date()
        
        self.system.book_room("John Doe", 101, check_in1, check_out1)
        
        # New booking after existing one
        check_in2 = datetime(2024, 12, 20).date()
        check_out2 = datetime(2024, 12, 25).date()
        
        available = self.system.is_room_available(101, check_in2, check_out2)
        self.assertTrue(available)
    
    def test_same_day_checkout_and_checkin(self):
        # First booking: Dec 10-15
        check_in1 = datetime(2024, 12, 10).date()
        check_out1 = datetime(2024, 12, 15).date()
        
        self.system.book_room("John Doe", 101, check_in1, check_out1)
        
        # Second booking: Dec 15-20 (same day checkout/checkin)
        check_in2 = datetime(2024, 12, 15).date()
        check_out2 = datetime(2024, 12, 20).date()
        
        # Should be available (checkout day is not occupied)
        available = self.system.is_room_available(101, check_in2, check_out2)
        self.assertTrue(available)


class TestDoubleBookingPrevention(unittest.TestCase):
    """Test that double booking is prevented"""
    
    def setUp(self):
        self.system = BookingSystem()
        self.system.add_room(101)
    
    def test_cannot_book_with_exact_same_dates(self):
        check_in = datetime(2024, 12, 10).date()
        check_out = datetime(2024, 12, 15).date()
        
        self.system.book_room("John Doe", 101, check_in, check_out)
        
        with self.assertRaises(RoomNotAvailableException):
            self.system.book_room("Jane Smith", 101, check_in, check_out)
    
    def test_cannot_book_when_dates_partially_overlap(self):
        check_in1 = datetime(2024, 12, 10).date()
        check_out1 = datetime(2024, 12, 15).date()
        
        self.system.book_room("John Doe", 101, check_in1, check_out1)
        
        check_in2 = datetime(2024, 12, 12).date()
        check_out2 = datetime(2024, 12, 17).date()
        
        with self.assertRaises(RoomNotAvailableException):
            self.system.book_room("Jane Smith", 101, check_in2, check_out2)
    
    def test_cannot_book_when_new_booking_spans_existing(self):
        check_in1 = datetime(2024, 12, 12).date()
        check_out1 = datetime(2024, 12, 15).date()
        
        self.system.book_room("John Doe", 101, check_in1, check_out1)
        
        # New booking completely contains existing booking
        check_in2 = datetime(2024, 12, 10).date()
        check_out2 = datetime(2024, 12, 20).date()
        
        with self.assertRaises(RoomNotAvailableException):
            self.system.book_room("Jane Smith", 101, check_in2, check_out2)
    
    def test_can_book_different_dates(self):
        check_in1 = datetime(2024, 12, 10).date()
        check_out1 = datetime(2024, 12, 15).date()
        
        self.system.book_room("John Doe", 101, check_in1, check_out1)
        
        check_in2 = datetime(2024, 12, 20).date()
        check_out2 = datetime(2024, 12, 25).date()
        
        booking = self.system.book_room("Jane Smith", 101, check_in2, check_out2)
        self.assertIsNotNone(booking)


class TestCancelBooking(unittest.TestCase):
    """Test booking cancellation"""
    
    def setUp(self):
        self.system = BookingSystem()
        self.system.add_room(101)
    
    def test_cancel_existing_booking(self):
        check_in = datetime(2024, 12, 10).date()
        check_out = datetime(2024, 12, 15).date()
        
        booking = self.system.book_room("John Doe", 101, check_in, check_out)
        cancelled = self.system.cancel_booking(booking.reference_id)
        
        self.assertTrue(cancelled.is_cancelled)
        self.assertEqual(cancelled.reference_id, booking.reference_id)
    
    def test_room_becomes_available_after_cancellation(self):
        check_in = datetime(2024, 12, 10).date()
        check_out = datetime(2024, 12, 15).date()
        
        booking = self.system.book_room("John Doe", 101, check_in, check_out)
        self.system.cancel_booking(booking.reference_id)
        
        available = self.system.is_room_available(101, check_in, check_out)
        self.assertTrue(available)
    
    def test_cannot_cancel_nonexistent_booking(self):
        with self.assertRaises(InvalidBookingException):
            self.system.cancel_booking("INVALID123")
    
    def test_cannot_cancel_already_cancelled_booking(self):
        check_in = datetime(2024, 12, 10).date()
        check_out = datetime(2024, 12, 15).date()
        
        booking = self.system.book_room("John Doe", 101, check_in, check_out)
        self.system.cancel_booking(booking.reference_id)
        
        with self.assertRaises(InvalidBookingException):
            self.system.cancel_booking(booking.reference_id)


class TestModifyBookingDates(unittest.TestCase):
    """Test modifying booking dates"""
    
    def setUp(self):
        self.system = BookingSystem()
        self.system.add_room(101)
    
    def test_modify_dates_when_available(self):
        check_in = datetime(2024, 12, 10).date()
        check_out = datetime(2024, 12, 15).date()
        
        booking = self.system.book_room("John Doe", 101, check_in, check_out)
        
        new_check_in = datetime(2024, 12, 20).date()
        new_check_out = datetime(2024, 12, 25).date()
        
        modified = self.system.modify_booking_dates(
            booking.reference_id, new_check_in, new_check_out
        )
        
        self.assertEqual(modified.check_in, new_check_in)
        self.assertEqual(modified.check_out, new_check_out)
    
    def test_cannot_modify_to_invalid_dates(self):
        check_in = datetime(2024, 12, 10).date()
        check_out = datetime(2024, 12, 15).date()
        
        booking = self.system.book_room("John Doe", 101, check_in, check_out)
        
        new_check_in = datetime(2024, 12, 25).date()
        new_check_out = datetime(2024, 12, 20).date()  # Before check-in!
        
        with self.assertRaises(InvalidBookingException):
            self.system.modify_booking_dates(
                booking.reference_id, new_check_in, new_check_out
            )
    
    def test_cannot_modify_when_new_dates_overlap_other_booking(self):
        # First booking
        check_in1 = datetime(2024, 12, 10).date()
        check_out1 = datetime(2024, 12, 15).date()
        booking1 = self.system.book_room("John Doe", 101, check_in1, check_out1)
        
        # Second booking
        check_in2 = datetime(2024, 12, 20).date()
        check_out2 = datetime(2024, 12, 25).date()
        self.system.book_room("Jane Smith", 101, check_in2, check_out2)
        
        # Try to modify first booking to overlap with second
        new_check_in = datetime(2024, 12, 18).date()
        new_check_out = datetime(2024, 12, 22).date()
        
        with self.assertRaises(RoomNotAvailableException):
            self.system.modify_booking_dates(
                booking1.reference_id, new_check_in, new_check_out
            )


class TestCalculateCost(unittest.TestCase):
    """Test booking cost calculation"""
    
    def setUp(self):
        self.system = BookingSystem()
        self.system.add_room(101, 'standard')  # $100/night
    
    def test_single_night_cost(self):
        check_in = datetime(2024, 12, 10).date()  # Tuesday
        check_out = datetime(2024, 12, 11).date()
        
        booking = self.system.book_room("John Doe", 101, check_in, check_out)
        cost = self.system.calculate_cost(booking)
        
        self.assertEqual(cost, 100.0)
    
    def test_multiple_nights_cost(self):
        check_in = datetime(2024, 12, 10).date()  # Tuesday
        check_out = datetime(2024, 12, 15).date()  # Sunday (5 nights)
        
        booking = self.system.book_room("John Doe", 101, check_in, check_out)
        cost = self.system.calculate_cost(booking)
        
        # 5 nights at $100, includes Fri+Sat (+$40 weekend surcharge)
        # Base: 5 * 100 = 500
        # Weekend surcharge: 2 * 100 * 0.20 = 40
        # Total: 540
        self.assertEqual(cost, 540.0)
    
    def test_extra_guest_fee(self):
        self.system.add_room(201, 'deluxe')  # $150/night, capacity 3
        
        check_in = datetime(2024, 12, 10).date()  # Tuesday
        check_out = datetime(2024, 12, 12).date()  # 2 nights
        
        # Book with 3 guests (1 extra beyond base 2)
        booking = self.system.book_room("John Doe", 201, check_in, check_out, num_guests=3)
        cost = self.system.calculate_cost(booking)
        
        # Base: 2 nights * $150 = 300
        # Extra guest: 1 guest * 2 nights * $25 = 50
        # Total: 350
        self.assertEqual(cost, 350.0)
    
    def test_seven_night_discount(self):
        check_in = datetime(2024, 12, 2).date()  # Monday
        check_out = datetime(2024, 12, 9).date()  # 7 nights
        
        booking = self.system.book_room("John Doe", 101, check_in, check_out)
        cost = self.system.calculate_cost(booking)
        
        # 7 nights at $100 = 700
        # Weekend surcharge: 2 nights * $100 * 0.20 = 40
        # Subtotal: 740
        # 10% discount: 740 * 0.90 = 666
        self.assertEqual(cost, 666.0)
    
    def test_fourteen_night_discount(self):
        check_in = datetime(2024, 12, 2).date()  # Monday
        check_out = datetime(2024, 12, 16).date()  # 14 nights
        
        booking = self.system.book_room("John Doe", 101, check_in, check_out)
        cost = self.system.calculate_cost(booking)
        
        # 14 nights at $100 = 1400
        # Weekend surcharge: 4 nights * $100 * 0.20 = 80
        # Subtotal: 1480
        # 15% discount: 1480 * 0.85 = 1258
        self.assertEqual(cost, 1258.0)


class TestRefundCalculation(unittest.TestCase):
    """Test cancellation refund policy"""
    
    def setUp(self):
        self.system = BookingSystem()
        self.system.add_room(101)
    
    def test_full_refund_seven_days_before(self):
        check_in = datetime(2024, 12, 20).date()
        check_out = datetime(2024, 12, 25).date()
        
        booking = self.system.book_room("John Doe", 101, check_in, check_out)
        
        cancellation_date = datetime(2024, 12, 10).date()  # 10 days before
        refund = self.system.calculate_refund(booking.reference_id, cancellation_date)
        
        total_cost = self.system.calculate_cost(booking)
        self.assertEqual(refund, total_cost)
    
    def test_fifty_percent_refund_three_to_six_days(self):
        check_in = datetime(2024, 12, 20).date()
        check_out = datetime(2024, 12, 25).date()
        
        booking = self.system.book_room("John Doe", 101, check_in, check_out)
        
        cancellation_date = datetime(2024, 12, 15).date()  # 5 days before
        refund = self.system.calculate_refund(booking.reference_id, cancellation_date)
        
        total_cost = self.system.calculate_cost(booking)
        self.assertEqual(refund, total_cost * 0.5)
    
    def test_no_refund_within_two_days(self):
        check_in = datetime(2024, 12, 20).date()
        check_out = datetime(2024, 12, 25).date()
        
        booking = self.system.book_room("John Doe", 101, check_in, check_out)
        
        cancellation