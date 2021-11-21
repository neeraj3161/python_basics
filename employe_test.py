import unittest
from employee_salary import Employee

class Testing_employee(unittest.TestCase):
    def setUp(self):
        self.employee_data=Employee('Raju','Jalnilla',200)
    def test_give_custom_raise(self):
        amount=200
        self.employee_data.give_custom_raise(amount)
        final_value=self.employee_data.annual_salary+amount
        self.assertIn(str(final_value),str(self.employee_data.final_salaryy))
    def test_give_default_raise(self):
        self.employee_data.give_raise_default()
        final_default_pay=self.employee_data.annual_salary+5000
        self.assertIn(str(final_default_pay),str(self.employee_data.default_final_salary))


