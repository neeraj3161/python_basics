
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 402 | 408:
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"


error = http_error(402)
print(error)


 # Note the last block: the “variable name” _ acts as a wildcard and never fails to match. If no case matches, none of the
 # branches is executed.


 # you can also combine this



# Patterns can look like unpacking assignments, and can be used to bind variables:
# match point:
# case (0, 0):
# print("Origin")
# case (0, y):
# print(f"Y={y}")
# case (x, 0):
# print(f"X={x}")
# case (x, y):
# print(f"X={x}, Y={y}")
# case _:
# raise ValueError("Not a point")

