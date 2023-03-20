# Logic Operators
# in | not in

# 0 1 2 3 4
# L U C A S
# 5 4 3 2 1

name = 'Lucas'

print('c' in name)
print('x' in name)
print('Luc' in name)
print('Isa' in name)
print(10 * '-')
print('Isa' not in name)
print(10 * '-')

name = input('Type name: ')
find = input('Type search text: ')

if find in name:
    print(f'{find} está em {name}')
else: 
    print(f'{find} não está em {name}')