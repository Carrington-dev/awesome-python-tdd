Here are some TDD assignment questions for a booking system:

## Assignment: Hotel Room Booking System (TDD Approach)

### Part 1: Basic Booking Operations

**Question 1: Create a Booking**
Implement functionality to create a new booking. A booking should have:
- Guest name
- Room number
- Check-in date
- Check-out date
- Booking reference (auto-generated unique ID)

Write tests first that verify:
- A booking can be created with valid data
- Booking reference is automatically generated and unique
- Check-out date must be after check-in date
- Required fields cannot be empty

**Question 2: Check Room Availability**
Implement a method to check if a room is available for given dates.

Write tests for:
- Room is available when no bookings exist
- Room is unavailable when dates overlap with existing booking
- Room is available when requested dates are before/after existing bookings
- Same-day checkout and check-in (checkout at 11am, new checkin at 2pm) - decide and test your business rule

**Question 3: Prevent Double Booking**
Implement logic to prevent booking a room that's already reserved.

Write tests for:
- Cannot book room with exact same dates as existing booking
- Cannot book room when dates partially overlap
- Cannot book room when new booking spans existing booking
- Cannot book room when new booking is contained within existing booking
- Can book room for different dates

### Part 2: Booking Modifications

**Question 4: Cancel a Booking**
Implement booking cancellation functionality.

Write tests for:
- Successfully cancel an existing booking
- Room becomes available after cancellation
- Cannot cancel a booking that doesn't exist
- Cannot cancel an already cancelled booking
- Cancelled bookings are marked (not deleted) for audit purposes

**Question 5: Modify Booking Dates**
Implement functionality to change check-in/check-out dates of existing booking.

Write tests for:
- Successfully modify dates when room is available
- Cannot modify if new dates overlap with another booking
- Cannot modify to invalid dates (checkout before checkin)
- Original booking is updated, not duplicated

### Part 3: Pricing & Calculations

**Question 6: Calculate Booking Cost**
Implement cost calculation based on number of nights and room rate.

Write tests for:
- Single night stay calculation
- Multiple night stay calculation
- Different room rates (standard: $100, deluxe: $150, suite: $200)
- Zero or negative duration returns error

**Question 7: Apply Discounts**
Implement discount logic for bookings.

Write tests for:
- 10% discount for stays of 7+ nights
- 15% discount for stays of 14+ nights
- Weekend surcharge: 20% extra for Friday/Saturday nights
- Discounts and surcharges are calculated correctly together

**Question 8: Calculate Refund Amount**
Implement cancellation refund policy.

Write tests for:
- Full refund if cancelled 7+ days before check-in
- 50% refund if cancelled 3-6 days before check-in
- No refund if cancelled within 2 days of check-in
- No refund for cancellations after check-in date

### Part 4: Advanced Features

**Question 9: List Bookings**
Implement methods to retrieve bookings with filters.

Write tests for:
- Get all bookings for a specific room
- Get all bookings for a specific guest
- Get all bookings within a date range
- Get upcoming bookings only (future check-ins)
- Get active bookings (currently checked in)

**Question 10: Room Capacity Management**
Implement guest count validation (assume rooms have max capacity).

Write tests for:
- Room capacity limits (standard: 2, deluxe: 3, suite: 4)
- Cannot book with more guests than room capacity
- Can book with fewer guests than capacity
- Extra guest fee: $25/night per guest above 2

**Question 11: Seasonal Pricing**
Implement dynamic pricing based on season.

Write tests for:
- Peak season (Dec-Feb, Jun-Aug): 1.5x base rate
- Off-peak season (Mar-May, Sep-Nov): base rate
- Calculate total cost correctly when booking spans seasons
- Weekend surcharge applies to seasonal rate

**Question 12: Waitlist Management**
When room is unavailable, add guest to waitlist.

Write tests for:
- Add guest to waitlist when room unavailable
- Notify/promote first waitlisted guest when booking cancelled
- Remove from waitlist when they book different dates
- Waitlist ordered by request date (first come, first served)

---

## Bonus Challenges

**Question 13: Multiple Room Booking**
Allow booking multiple rooms in single reservation.

**Question 14: Loyalty Points**
Award points: 10 points per dollar spent, implement redemption (100 points = $1 discount).

**Question 15: Payment Status Tracking**
Track payment status: pending, partial, paid, refunded with state transitions.

---

## Instructions

For each question:
1. **Write the test first** (Red phase)
2. **Make it pass with minimal code** (Green phase)
3. **Refactor** for clean code (Refactor phase)
4. Run all previous tests to ensure nothing broke

Start simple with Question 1 and progress sequentially. Each question builds on previous functionality.

Which questions would you like to start with?
