# Flags
# None, is, is not, id

# ids
v1 = 'a'
v2 = 'b'
# print(id(v1))
# print(id(v2))

# ---------------

condition = False
if_passed = None

if condition:
    if_passed = True
    print('do something')
else:
    print("don't do")

if if_passed is None:
    print('If not passed')
else: 
    print('If passed')