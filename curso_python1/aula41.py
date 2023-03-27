# while / else
# when while find a break else is not executed
# should be used when a if with a break is not found
string = 'any value'

i = 0
while i < len(string):
    letter = string[i]

    print(letter)
    i += 1
else: 
    print('else executed')