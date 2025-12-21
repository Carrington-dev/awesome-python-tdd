import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG,
    # add streamHandler or fileHandler if needed
    handlers = [
        logging.StreamHandler(),
        logging.FileHandler('logs/lms.log')  # Uncomment to log to a file
    ]
)

logger = logging.getLogger(__name__)

class Library:
    """
    Docstring for Library

    The instance which represents the Library
    """
    def __init__(self, name):
        self.name = name
        self.reading_units = {}
        self.librarians = {}
        self.cart = {}
    
    def get_reading_materials(self):
        return self.reading_units

    def get_librarians(self):
        return self.librarians
    
    def book_reading_material_unit(self, reading_material: ReadingMaterialUnit):
        if reading_material.isbn not in self.cart:
            self.cart[reading_material.isbn] = True
        else:
            logger.info(f"{reading_material.isbn} is already reserved for this user")
            raise Exception(f"{reading_material.isbn} is already reserved for this user")

class ReadingMaterialUnit:
    """
    Docstring for ReadingMaterialUnit
    
    """

    def __init__(self, title, author, year_published, isbn, typr_ = "book"):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.isbn = isbn
        self.type = typr_

    def __str__(self):
        return f"ReadingMaterialUnit({self.title=}, {self.author=}, {self.isbn=})"

reading_material_unit = ReadingMaterialUnit("New Maths", "author", "isbn", "year_published")
 
print(reading_material_unit)