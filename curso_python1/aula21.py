# Logic Operators
# and | or | not
# Falsy -> 0 | 0.0 | False | None

# Example 1
# inp = input('[E]ntrar [S]air: ')
# password = input('Senha: ')

# allowed_password = '123456'

# if inp == 'E' and password == allowed_password:
#     print('Entrar')
# else:
#     print('Sair')

# Example 2
print(True and True and False) #False
print(True and True and True) #True
print(1 and True and True) #True
print(True and 0 and True) #0

if 1 and 1:
    print(True and 1) #0