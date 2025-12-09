import uuid
import logging
from datetime import datetime, timedelta

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG,
    # add streamHandler or fileHandler if needed
    handlers = [
        logging.StreamHandler(),
        logging.FileHandler('logs/booking.log')  # Uncomment to log to a file
    ]
)


logger = logging.getLogger(__name__)

def generate_checkout_date(number_of_days = 1):
    date_today = datetime.now() + timedelta(days = number_of_days)
    return date_today

user_list = {
    '0168154259082': {'age': 45, 'full_name': 'Steven Miller', 'id': '0168154259082'},
    '1047745271084': {'age': 60, 'full_name': 'Jeffrey Holland', 'id': '1047745271084'},
    '1474505146084': {'age': 49, 'full_name': 'James Rodriguez', 'id': '1474505146084'},
    '1536313871081': {'age': 24, 'full_name': 'Lisa Peterson', 'id': '1536313871081'},
    '1768061462085': {'age': 33, 'full_name': 'Jeffrey Weaver', 'id': '1768061462085'},
    '1854454228083': {'age': 26, 'full_name': 'Darren Anderson', 'id': '1854454228083'},
    '3047244456088': {'age': 40, 'full_name': 'Jeremy Peterson', 'id': '3047244456088'},
    '3527653046089': {'age': 29, 'full_name': 'Jeffrey Kramer', 'id': '3527653046089'},
    '3541180845084': {'age': 38, 'full_name': 'Michelle Garcia', 'id': '3541180845084'},
    '5132921360089': {'age': 54, 'full_name': 'Anna Wood', 'id': '5132921360089'},
    '5470790388087': {'age': 51, 'full_name': 'Brian Stevens', 'id': '5470790388087'},
    '6235335312080': {'age': 26, 'full_name': 'Christina Kelly', 'id': '6235335312080'},
    '6292344283081': {'age': 27, 'full_name': 'Amber Garcia', 'id': '6292344283081'},
    '6930543883084': {'age': 60, 'full_name': 'Amy Jones', 'id': '6930543883084'},
    '7078761819086': {'age': 58, 'full_name': 'Dr. Matthew Carpenter', 'id': '7078761819086'},
    '7572026002087': {'age': 35, 'full_name': 'Susan Carpenter', 'id': '7572026002087'},
    '8265805005085': {'age': 47, 'full_name': 'Joe Bishop', 'id': '8265805005085'},
    '8988902781080': {'age': 36, 'full_name': 'Michael Hale', 'id': '8988902781080'},
    '9037816322084': {'age': 21, 'full_name': 'Scott Franklin', 'id': '9037816322084'},
    '9760205353082': {'age': 32, 'full_name': 'Angelica Johnson', 'id': '9760205353082'}
}

class Booking:
    def __init__(self, 
                 age=23,  
                 id = "9760205353087", 
                 full_name = "John Doe", 
                 room_number = 1, check_in_date = datetime.now(), 
                 check_out_date = generate_checkout_date(2)):
        self.id = id
        self.age = age
        self.full_name = full_name
        self.room_number = room_number
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.booking_reference = str(uuid.uuid4())

    def __str__(self):
        return f"Booking(full_name={self.full_name}, id={self.booking_reference})"


class ReversationSystem:
    def __init__(self, total_bookings_per_day = 20):
        self.bookings = {}
        self.TOTAL_BOOKINGS_PER_DAY = total_bookings_per_day
        self.user_list = user_list

    def book_for_user_by_id(self, id_number: str, number_of_days = 1, number_of_rooms = 1):
        """
        Docstring for book_for_user_by_id
        
        :param self: book a hotel by user id
        :param id_number: User Id number from DHA
        :type id_number: str
        :param number_of_days: Number of days booked for
        :param number_of_rooms: Number of rooms booked for
        """
        if id_number not in self.user_list:
            raise Exception("User must be registered with Home Affairs")
        elif id_number in self.bookings:
            raise Exception(f"{ id_number } is already booked, try increasing rooms instead")
        elif self.is_fully_booked():
            raise Exception(f"Hotel is fully booked")
        
        booking =  Booking(**self.user_list[id_number])
        booking_info = self.bookings[id_number] = {
            "booking": booking,
            "booking_reference": booking.booking_reference,
            "number_of_rooms": number_of_rooms,
            "number_of_days": number_of_days,
        }
        logger.debug(f"User with id_number: {id_number} has successfully booking a hotel, reference: {booking.booking_reference}")
        logger.debug( booking_info )
        return booking_info

    
    def is_fully_booked(self):
        return False
    
