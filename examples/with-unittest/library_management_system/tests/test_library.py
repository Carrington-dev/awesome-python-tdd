import unittest
from main import Library, ReadingMaterialUnit

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library("name of library")

    def tearDown(self):
        self.library = None

    def test_library_creation(self):
        """
        Docstring for test_library_has_reading_units
        Testing to see if the Library has reading units like books, articles, newspapers etc
        
        :param self: calls the TestLibrary Instance
        """
        self.assertTrue(self.library.name, "name of library")

    def test_library_has_reading_units(self):
        """
        Docstring for test_library_has_reading_units
        Testing to see if the Library has reading units like books, articles, newspapers etc
        
        :param self: calls the TestLibrary Instance
        """
        self.assertTrue(type(self.library.reading_units), dict)

    def test_library_has_librarians(self):
        """
        Docstring for test_library_has_librarians
        
        :param self: Description
        """
        self.assertNotEqual(self.library.librarians, None)
        self.assertTrue(type(self.library.librarians), dict)

    def test_library_booking_checkout(self):
        """
        Docstring for test_library_booking_checkout
        
        :param self: Description
        :param reading_material: reading material
        """
        reading_material = ReadingMaterialUnit("New Maths", "author", "isbn", "year_published")
        self.library.book_reading_material_unit(reading_material)
        self.assertTrue(1, len(self.library.get_reading_materials()))

    def test_library_booking_checkout_collision(self):
        """
        Docstring for test_library_booking_checkout
        
        :param self: Description
        :param reading_material: reading material
        """
        reading_material = ReadingMaterialUnit("New Maths", "author", "isbn", "year_published")
        reading_material2 = ReadingMaterialUnit("New Maths", "author", "isbn", "year_published")
        self.library.book_reading_material_unit(reading_material)
        with self.assertRaises(Exception):
            self.library.book_reading_material_unit(reading_material2)
        # self.assertTrue(1, len(self.library.get_reading_materials()))

    def test_library_booking_system_cancellelation(self):
        """
        Docstring for test_library_has_librarians
        
        :param self: Description
        """
        pass

