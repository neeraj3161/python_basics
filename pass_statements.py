# while True:
# The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no
# action. For example:


while True:
    pass

    # if you don't use pass and leave it as it is you will get a error
#
#     ^
# IndentationError: expected an indented block

# This is commonly used for creating minimal classes:

class MyFirstClass:
    pass

# Another place pass can be used is as a place-holder for a function or conditional body when you are working on new
# code, allowing you to keep thinking at a more abstract level. The pass is silently ignored:

def func(*args):
    pass

# if you see the program keeps running as this is a place holder