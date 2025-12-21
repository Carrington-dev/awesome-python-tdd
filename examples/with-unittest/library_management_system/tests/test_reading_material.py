import unittest
from main import ReadingMaterialUnit

class TestReadingMaterialUnit(unittest.TestCase):
    def setUp(self):
        self.reading_material_unit = ReadingMaterialUnit(title="title", author="author", isbn="isbn", year_published="year_published")
    
    def tearDown(self):
        self.reading_material_unit = None

    def test_reading_material_creation(self):
        self.assertEqual(self.reading_material_unit.title, "title")
        self.assertEqual(self.reading_material_unit.author, "author")
        self.assertEqual(self.reading_material_unit.isbn, "isbn")
        self.assertEqual(self.reading_material_unit.year_published, "year_published")

    def test_reading_material_creation_type(self):
        self.assertEqual(self.reading_material_unit.type, "book")
    
    def test_reading_material_string_representation(self):
        self.assertIn(self.reading_material_unit.title, str(self.reading_material_unit))
        self.assertIn(self.reading_material_unit.author, str(self.reading_material_unit))

    