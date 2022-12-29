import unittest


class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, d_salary=5000):
        self.salary += d_salary
        return self.salary


class Tempolory(unittest.TestCase):
    def setUp(self) -> None:
        self.my_employee = Employee('zhang', 'zheng', 0)

    def test_give_default_raise(self):
        self.assertEqual(5000, self.my_employee.give_raise())

    def test_give_custom_raise(self):
        given_raise = 1000
        self.assertEqual(given_raise, self.my_employee.give_raise(given_raise))
