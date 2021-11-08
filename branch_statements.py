def is_positive(number):
  if number>0:
    return number
print(is_positive(-1))

# here we are branching diff statements together

# if Statements Recap
# We can use the concept of branching to have our code alter its execution sequence depending on the values of variables. We can use an if statement to evaluate a comparison. We start with the if keyword, followed by our comparison. We end the line with a colon. The body of the if statement is then indented to the right. If the comparison is True, the code inside the if body is executed. If the comparison evaluates to False, then the code block is skipped and will not be run.

# def user_name(userName):
#   if len(userName)<3:
#     print("Invalid user name it should be atleast 3 characters")
#   else:
#     print("Valid username")
# user_name('Neeraj')

# when a return statement is executed the code exits so that the code that follow doesn't gets executed or it will be executed a trick to avoid the else statement'

def func1(name):
  if len(name)<3:
    return "Invalid name"
  return "Valid name"

name_print = func1('Neeraj')
print(name_print)

def even_num(number):
  if number%2==0:
    return "Even Number"   #true e statement
  return "Odd number"      #fals

print(even_num(266))

# else Statements and the Modulo Operator
# We just covered the if statement, which executes code if an evaluation is true and skips the code if it’s false. But what if we wanted the code to do something different if the evaluation is false? We can do this using the else statement. The else statement follows an if block, and is composed of the keyword else followed by a colon. The body of the else statement is indented to the right, and will be expected if the above if statement doesn’t execute.
#
# We also touched on the modulo operator, which is represented by the percent sign: %. This operator performs integer division, but only returns the remainder of this division operation. If we’re dividing 5 by 2, the quotient is 2, and the remainder is 1. Two 2s can go into 5, leaving 1 left over. So 5%2 would return 1. Dividing 10 by 5 would give us a quotient of 2 with no remainder, since 5 can go into 10 twice with nothing left over. In this case, 10%2 would return 0, as there is no remainder.

def user_name(userName):
  if len(userName)<3:
    print("Invalid user name it should be atleast 3 characters")
  elif len(userName)>15:
      print('Username should be less than 15 characters')
  else:
    print('valid username')
      # else:
      # print("Valid username") #unwanted nesting
      # this will through a error
          # use elif to add multiple conditions

user_name('Neerafgdfhdfgjdhfjhdhfjhsdjhfdkhfjj')

# More Complex Branching with elif Statements
# Building off of the if and else blocks, which allow us to branch our code depending on the evaluation of one statement, the elif statement allows us even more comparisons to perform more complex branching. Very similar to the if statements, an elif statement starts with the elif keyword, followed by a comparison to be evaluated. This is followed by a colon, and then the code block on the next line, indented to the right. An elif statement must follow an if statement, and will only be evaluated if the if statement was evaluated as false. You can include multiple elif statements to build complex branching in your code to do all kinds of powerful things!