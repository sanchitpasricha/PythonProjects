alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, number, direction):
    final_text = ""

    for letter in plain_text:
        position = alphabets.index(letter)
        if direction == 'encode':
            new_position = position + number
        else:
            new_position = position - number
        new_letter = alphabets[new_position]
        final_text += new_letter

    return final_text
