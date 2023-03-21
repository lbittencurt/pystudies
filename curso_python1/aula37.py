# While
counter = 0

while counter <= 10:
    counter += 1
    
    if counter == 2:
        continue  # skip 2 from print

    print(counter)

    if counter == 4:
        print(f'counter {counter}')
        break


print('System end.')