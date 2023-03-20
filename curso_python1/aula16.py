# if / elif / else
user_input = input('Do you want to "enter" or to "leave"? ')

if user_input == 'enter':
    print('You are in the system.')
elif user_input == 'leave':
    print('You are out of the system.')
else:
    print('Invalid option.')
    
print('Out of block.')