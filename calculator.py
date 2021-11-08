# first project



def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def percentage(x, y):
    return round(x / y * 100)


def sqrt(x,y):
    return x**y

while True:
    operation = input('please select the operator e.g +,-,*,%,** :')
    if operation in ('+', '-', '*', '%','**'):
        num1 = int(input('Enter number 1 :'))
        num2 = int(input('Enter number 2 :'))
    else:
        print("Invalid operator")
        print("start again please enter a correct operator from examples")
        break
    if operation == '+':
        print('Addition of ', num1, 'and ', num2, ' is ', add(num1, num2))
    elif operation == '-':
        print('Subtraction of ', num1, 'and ', num2, ' is ', subtract(num1, num2))
    elif operation == '**':
        print('Square root of ', num1, 'over ', num2, ' is ', sqrt(num1, num2))
    elif operation == '*':
        print('Multiplication of ', num1, 'and ', num2, ' is ', multiply(num1, num2))
    elif operation == '%':
        print('Percentage of ', num1, 'by ', num2, ' is ', percentage(num1, num2), '%')
    continue_calc = input("Would you like to continue calculating(y/n): ")
    if continue_calc == 'n':
        print("Thank you for using Calculator ❤️")
        break
    elif continue_calc == 'y':
        print("Starting again...")
    else:
        print("Invalid Input")
        break



