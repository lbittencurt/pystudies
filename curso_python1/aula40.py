# While calc
while True:
    number_1 = input('Type a number: ')
    number_2 = input('Type other: ')
    operator = input('Type operator (+-/*): ')
    
    valid_numbers = None

    number_1_float = 0
    number_2_float = 0

    try:
        number_1_float = float(number_1)
        number_2_float = float(number_2)
        valid_numbers = True
    except:
        valid_numbers = None

    if valid_numbers is None:
        print('One or more number are invalid.')
        continue

    valid_operators = '+-/*'

    if operator not in valid_operators or len(operator) != 1:
        print('Invalid operator.')
        continue

    print('Calculating...')
    if operator == '+':
        print(f'Result: {number_1_float + number_2_float}')
    elif operator == '-':
        print(f'Result: {number_1_float - number_2_float}')
    elif operator == '/':
        print(f'Result: {number_1_float / number_2_float}')
    elif operator == '*':
        print(f'Result: {number_1_float * number_2_float}')
    else:
        print('Unexpected error.')
        continue

    exit = input('Do you want to exit? [y]es: ')
    if exit.lower().startswith('y'):
        print(exit)
        break

print('system end')
