import unittest
from employees import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        """Create an employee to test all methods."""
        self.tyson = Employee('Tyson', 'Nguyen', 20000)

    def test_give_default_raise(self):
        """Test to see if default value adds to the salary."""
        self.tyson.give_raise()
        self.assertEqual(self.tyson.salary, 25000)

    def test_give_custom_raise(self):
        """Test a custom value for raise to salary works."""
        self.tyson.give_raise(10000)
        self.assertEqual(self.tyson.salary, 30000)

if __name__ == '__main__':
    unittest.main()