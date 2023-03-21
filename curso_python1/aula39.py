# Iterating over string with while
#       0123456789
name = 'Lucas Bittencurt'
name_len = len(name)

# new_string += '*L*'
new_string = ''
index = 0
while index < name_len:
    new_string += f'*{name[index]}'
    index += 1

print(new_string)