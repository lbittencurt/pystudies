"""
Split strings
"""
variable = 'Olá mundo'
print(variable[5])  # -> u
print(variable[-4])  # -> u
print(variable[4:])  # -> mundo
print(variable[4:8])  # -> mund
print(variable[:5])  # -> Olá m

print(10 * '-')

print(len(variable))  # -> 9
print(variable[0:9:2])  # -> Oámno
print(variable[::-1])  # -> odnum álO