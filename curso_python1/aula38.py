# Loops While

qtd_lines = 5
qtd_columns = 5

line = 1
while line <= qtd_lines:
    column = 1
    while column <= qtd_columns:
        print(f'{line=} {column=}')
        column += 1
    line += 1

print('system end.')