# try/except

# print('before error')
# int('a')  # error: ValueError
number_str = input('Double this number: ')

try:
    number_float = float(number_str)
    print(f'Double: {number_float * 2:.2f}')
except:
    print('Input is not a number.')