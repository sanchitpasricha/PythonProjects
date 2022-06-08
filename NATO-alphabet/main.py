import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_words = {row.letter:row.code for (index, row) in data.iterrows()}
word = input("Enter a word you want nato word list for :: ")
word_letter_list = list(word.upper())
final_list = [nato_words[letter] for letter in word_letter_list]
print(final_list)