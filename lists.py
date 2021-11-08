squares = [1,2,3,4,5,6]
print(squares)

# list comes in [] square brackets

# we can also slice the list

print(squares[0:3])
# o se 3 ke pehle tak

print(squares[:])

print(squares[-1:10])

# -1 is the last item in the list we dont take -0 as -0 and 0 are same

# list are mutable while strings are not

squares[0]=10
print(squares)

# You can also add new items at the end of the list, by using the append() method (we will see more about methods
squares.append(12)
print(squares)

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:

squares[2:5]=[]
print(squares)

# will not print anything from 2 se 5 ke pehle tak

print(len(squares))




