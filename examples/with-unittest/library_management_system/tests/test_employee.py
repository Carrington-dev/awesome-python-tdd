import unittest

from main import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        """
        Docstring for setUp
        
        :param employee: Employee of the Library
        """
        self.employee = Employee(name="name", age=19, profession="cleaner")

    
    def tearDown(self):
        self.employee = None
    
    def test_employee_created(self):
        self.assertTrue(type(self.employee.name) == str)
        self.assertTrue(type(self.employee.profession) == str)
        self.assertTrue(type(self.employee.age) == int)
        self.assertTrue(type(self.employee.race) == str)

    def test_employee_has_not_retired(self):
        self.assertGreaterEqual((self.employee.age), 18)

    def test_employee_has_race(self):
        self.assertEqual(type(self.employee.race),  str)

    def test_employee_string_representation(self):
        self.assertIn(self.employee.name, str(self.employee))
        self.assertIn(str(self.employee.age), str(self.employee))
