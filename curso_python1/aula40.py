# While calc
while True:
    number_1 = input('Type a number: ')
    number_2 = input('Type other: ')
    number_3 = input('Type operator (+-/*): ')
    
    valid_numbers = None

    try:
        number_1_float = float(number_1)
        number_2_float = float(number_2)
        valid_numbers = True
    except:
        valid_numbers = None

    if valid_numbers is None:
        print('One or more number are invalid.')
        continue       

    sair = input('Quer sair? [s]im: ')
    if sair.lower().startswith('s'):
        print(sair)
        break

print('system end')
