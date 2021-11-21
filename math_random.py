# now lets import and use the classes developed by programmers

# let's have a look at one module which is math.random can be used for many real world examples'

from random import randint as ran
from random import choice as ch

print(ran(1,6))

# here the class randit gives out output of any random number from 1 to 6

names= ['John','Ganesh','Raju','Chris']
choice_name=ch(names)
print(choice_name)

# The random module shouldn’t be used when building security-related
# applications, but it’s good enough for many fun and interesting projects.

# You can also download modules from external sources. You’ll see a number of these
# examples in Part II, where we’ll need external modules to complete each project.

