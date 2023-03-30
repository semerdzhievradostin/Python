import pandas
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

user_input = input("Type a word that you want to code\n")
code_words = [nato_alphabet_dict[letter.upper()] for letter in user_input]
print(code_words)



