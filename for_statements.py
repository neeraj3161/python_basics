# Python’s for statement iterates over the items of any sequence (a list or a string), in the order
# that they appear in the sequence. For example (no pun intended):

words = ['cat','dog','window']

for w in words:
    print(w,len(w))

# list = [1,2,3,4,5]
#
# new_list = list.copy()
# # copy is used in python to copy the same item
# print(new_list)


# we are creating a copy and using a for loop to set out a filter
users = {
    'neeraj' : 'active',
    'ganesh' : 'inactive',
    'raju':'active'
}

# del is used to delete objects
# items is used to look items in the dictionary
# Strategy: Iterate over a copy
for name,stat in users.copy().items():
    if stat == 'active':
        del users[name]
print(users)


users = {
    'neeraj' : 'active',
    'ganesh' : 'inactive',
    'raju':'active'
}
# creating a new collection
active_users = {}
for name,status in users.items():
    if status == 'active':
        active_users[name]=status
print(active_users)

