class Employee:
    def __init__(self,first_name,last_name,Annual_salary):
        self.firstname=first_name
        self.lastname=last_name
        self.annual_salary=Annual_salary
        # print(f'{first_name.title()} {last_name.title()} your Annual salary was {Annual_salary} $')
    # def give_raise(self):
    #     take_input=input('Your default raise amount is 5000$ would you like to add a manual input (y/n) : ')
    #     if take_input=='y':
    #         manual_value=int(input("Enter your manual raise amount : "))
    #         if int(manual_value)>int(7000):
    #             print("You are not eligible for this amount!!!")
    #         else:
    #             final_salary=self.annual_salary+manual_value
    #             print(f'Your manual raise value is {str(final_salary)} $')
    #     elif take_input=='n':
    #         final_salary_default=int(self.annual_salary)+5000
    #         print(f'Your default raise value is {str(final_salary_default)} $')
    #         print(f'{self.firstname.title()} your salary now is {str(final_salary_default)} $')

    def give_raise_default(self):
        self.default_final_salary=self.annual_salary+5000

        # print(f'Your salary now is {str(final_salary)} $')

    def give_custom_raise(self,amount):
        self.final_salaryy=self.annual_salary+amount



employee=Employee('Raju','Jalnila',2000)
print(employee.give_custom_raise(200))
