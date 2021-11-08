for i in range(100):
    print(i,end=',')
print("\n")
# you can also have a range value
for i in range(5,10):
    print(i,end=" ")


# creates a list with the range statement
print(list(range(0,100)))

# you can also step between ranges

print(list(range(0,100,25)))
# the statement above will step at every 25 numbers

# To iterate over the indices of a sequence, you can combine range() and len() as follow
names = ['ganesh','raju','neeraj']
for i in range(len(names)):
    print(i,names[i])
print(range(0,10))

print(sum(range(0,10))) #>> 0+1+2+3+4+5+6+7+8+9
print(0+1+2+3+4+5+6+7+8+9) #you will understand what's its doing

