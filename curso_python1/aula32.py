"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
number_str = input('Type a integer number: ')
try:
    number_int = int(number_str)
    if number_int % 2 == 0:
        print(f'{number_int} is a even number.')
    else:
        print(f'{number_int} is a odd number.')        
except:
    print('Input is not a integer number.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hour_str = input('Type the current hour: ')
try:
    hour_int = int(hour_str)
    if hour_int >= 0 and hour_int <= 11:
        print(f'Good morning.')
    elif hour_int >= 12 and hour_int <= 17:
        print(f'Good afternoon.')
    elif hour_int >= 18 and hour_int <= 23:
        print(f'Good night.')
    else:
        print(f'Invalid hour number.')
except:
    print('Input is not a integer number.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
name = input('Type your first name: ')
name_len = len(name)
if name_len <= 4:
    print(f'You have a short name.')
elif name_len >= 5 and name_len <= 6:
    print(f'You have a normal name.')
else:
    print(f'You have a big name.')