from employee_salary import Employee


while True:
    first_name=input("Enter your first name : ")
    last_name=input('Enter your last name : ')
    Annual_salary=input("Enter your annual salary : ")
    emplyee_data=Employee(first_name,last_name,Annual_salary)
    emplyee_data.give_raise()

