# This is basically known as control flow statement

# Perhaps the most well-known statement type is the if statement. For example:

x=int(input("Please enter an integer : "))
if x<0:
    x=0
    print("Negative changed to zero")
    print(x)
elif x==0:
        print("zero")
elif x==1:
    print("Single Value")
else:
    print("Positive Value")

# There can be zero or more elif parts, and the else part is optional.
# The keyword ‘elif’ is short for ‘else if’, and is
# useful to avoid excessive indentation. An if … elif … elif … sequence is a substitute for the switch or case
# statements found in other languages for eg in JAVA

