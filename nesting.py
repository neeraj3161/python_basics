# It is possible to nest lists (create lists containing other lists), for example:

a=[1,2,3,4,5,6,7,8]
b=['a','b','c','d','e']
x=[a,b]
print(x)

# nesting is basically to add two list items together

# now here again we can take slice into consideration

indexing = x[0]
# here we are taking the first index of the list
print(indexing)

indexing_firstdigit = x[0][1]
print(indexing_firstdigit)

# here it prints the first first digit of 0 index in x


