"""
type convertion
- convertion
- typecasting
- coercion
[str, int, float, bool] imutables types
"""

# int + int
print(1 + 1)

# int + float
print(1 + 1.1)

# str + str
print('a' + 'b')

# str + int
# print('1' + 1) throw an TypeError
print(int('1') + 1)
print('1' + str(1))

# str + bool
# print('1' + True) throw an TypeError
print('1' + str(True))

# convertion to bool
print(bool(0))
print(bool(1))
print(bool(''))
print(bool('1'))

# convertion to float
print(float('1.0'))