from name_function import get_full_name

print('Enter q to exit anytime...')

while True:
    firstname=input('Please enter your first name :  \n')
    if firstname=='q':
        break
    lastname=input('Enter your last name : \n')
    if lastname=='q':
        break
    formatted_name=get_full_name(firstname,lastname)
    print(f'Neatly formatted name : {formatted_name}')