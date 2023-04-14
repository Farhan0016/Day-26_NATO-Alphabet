# TODO 1. Create a dictionary in this format:
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas as pd

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")

# Loop through rows of a data frame Keyword Method with iterrows()
phonetic_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

word = input("Enter a word: ").upper()

output_list = [phonetic_dict[letter] for letter in word if letter not in [' ', '.']]
print(output_list)
