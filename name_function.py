# Here we are using the python module unittest to test our program


def get_full_name(firstname,lastname):
    full_name=firstname+" "+lastname
    return full_name.title()

def get_formatted_name(firstname,middlename,lastname):
    formattted_full_name=firstname+" "+middlename+' '+lastname
    return formattted_full_name
