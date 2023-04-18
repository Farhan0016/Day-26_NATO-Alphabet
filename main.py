# TODO 1. Create a dictionary in this format:
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas as pd


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word if letter not in [' ', '.']]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


nato_df = pd.read_csv("nato_phonetic_alphabet.csv")

# Loop through rows of a DataFrame Keyword Method with iterrows()
phonetic_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

generate_phonetic()
