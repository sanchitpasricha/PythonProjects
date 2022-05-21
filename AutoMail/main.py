HEAD = '[name]'

with open('Input/Names/invited_names.txt') as name_file:
    names = name_file.read()
    names_list = names.split("\n")

with open('Input/Letters/starting_letter.txt') as body:
    letter = body.read()
    for name in names_list:
        final_letter = letter.replace(HEAD, name)
        with open(f'Output/ReadyToSend/letter_to_{name}.txt', mode='w') as edited_letter:
            edited_letter.write(final_letter)