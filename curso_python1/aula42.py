phrase = 'O Python é uma linguagem de programação '\
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'

# print(phrase.count('Python'))  # => 2

i = 0
appear_count = 0
letter_most_appear = ''

while i < len(phrase):
    actual_letter = phrase[i]
    i += 1

    if actual_letter == ' ':
        continue

    letter_count = phrase.count(actual_letter)

    if appear_count < letter_count:
        appear_count = letter_count
        letter_most_appear = actual_letter
else:
    print(f'Letter most appear: {letter_most_appear} ({appear_count})' )