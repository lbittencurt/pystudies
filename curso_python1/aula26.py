# strings format
# s - string
# d - int
# f - float
# .<numero de digitos>f
# x ou X - Hexadecimal
# (Caractere)(><^)(quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# Sinal - + ou -

var = 'ABC'
print(f'{var}')
print(f'{var: >10}.')
print(f'{var: <10}.')
print(f'{var:/>10}.')
print(f'{1000.8197298371289371:.1f}')
print(f'{-1000.8197298371289371:+,.1f}')
print(f'O hexadecimal de 1500 é: {1500:08X}')