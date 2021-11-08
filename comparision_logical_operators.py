print("cat">"Cat")
# This will give a boolean value and as in string c small alphabet is bigger than the large one

print(1==2)
print(1!=2)
print(1!='11')
print(1=='1')
# false because one i sint and one is string llet's change it below
print('1'=='1')


# Logical operators in python

# and , or and not

print('\n')

print("Yellow">'brown' and 'brown'>'magenta')
print(24>2 or 24<50)

# not operator inverts the value that's in front of it

print(not 42==42)
# the expression above is checking if 42 is not equal to 42

# In Python, we can use comparison operators to compare values. When a comparison is made, Python returns a boolean result, or simply a True or False.
#
# To check if two values are the same, we can use the equality operator: ==
#
# To check if two values are not the same, we can use the not equals operator: !=
#
# We can also check if values are greater than or lesser than each other using > and <. If you try to compare data types that aren’t compatible, like checking if a string is greater than an integer, Python will throw a TypeError.
#
# We can make very complex comparisons by joining statements together using logical operators with our comparison operators. These logical operators are and, or, and not. When using the and operator, both sides of the statement being evaluated must be true for the whole statement to be true. When using the or operator, if either side of the comparison is true, then the whole statement is true. Lastly, the not operator simply inverts the value of the statement immediately following it. So if a statement evaluates to True, and we put the not operator in front of it, it would become False.

print('A dog'>'A mouse')