# a,b=1,2
# while a<=10:
#     print(a)
#     a,b=b,a+b


# The while loop executes as long as the condition (here: a < 10) remains true


# This example introduces several new features.
# • The first line contains a multiple assignment: the variables a and b simultaneously get the new values 0 and 1. On
# the last line this is used again, demonstrating that the expressions on the right-hand side are all evaluated first before
# any of the assignments take place. The right-hand side expressions are evaluated from the left to the right.

# standard operators for while loop
# The standard comparison operators are written the same as in C: < (less than), > (greater than), == (equal to), <=
# (less than or equal to), >= (greater than or equal to) and != (not equal to).

# • The body of the loop is indented: indentation is Python’s way of grouping statements.
#
# c,d = 0,1
# while c<=10000:
#     print(c,end=",")
#     c,d=d,c+d

# here we use the end method to seperate or end the given outplut with the end value provided

# def main():
#     x=0
#     while (x<5):
#         print(x)
#         x=x+1
# if __name__ == '__main__':
#     main()
# two ways of looping while and for

# for x in range (5,10+1):
#     print(x)
#
# days=["Mon","True",'Thu','fri' ,'sat','sun']
#
# for d in days:
#     print(d)

# for x in range(5,10):
#     if (x==7):
#         break
#     print(x)


days=["Mon","True",'Thu','fri' ,'sat','sun']

for i,d in enumerate (days):
    print(i,d)

    # enumarate also adds indexing

# Common Pitfalls With Variable Initialization
# You'll want to watch out for a common mistake: forgetting to initialize variables. If you try to use a variable without first initializing it, you'll run into a NameError. This is the Python interpreter catching the mistake and telling you that you’re using an undefined variable. The fix is pretty simple: initialize the variable by assigning the variable a value before you use it.
#

# Another common mistake to watch out for that can be a little trickier to spot is forgetting to initialize variables with the correct value. If you use a variable earlier in your code and then reuse it later in a loop without first setting the value to something you want, your code may wind up doing something you didn't expect. Don't forget to initialize your variables before using them!

# in python we use the break keyword to break the loop

# Infinite loops and Code Blocks
# Another easy mistake that can happen when using loops is introducing an infinite loop. An infinite loop means the code block in the loop will continue to execute and never stop. This can happen when the condition being evaluated in a while loop doesn't change. Pay close attention to your variables and what possible values they can take. Think about unexpected values, like zero.
#
# In the Coursera code blocks, you may see an error message that reads "Evaluation took more than 5 seconds to complete." This means that the code encountered an infinite loop, and it timed out after 5 seconds. You should take a closer look at the code and variables to spot where the infinite loop is.