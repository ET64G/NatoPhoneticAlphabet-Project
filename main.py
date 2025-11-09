import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")

# SYNTAX {new_key:new_value for (index, row) in df.writerows()}
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}

cont = False

while not cont:
    # list separates word into letters, converts to uppercase
    word = list(input("Enter a Word: ").upper())

    # SYNTAX: upper_name = [new_item for item in list if test]
    try:
        code_words = [phonetic_dict[letter] for letter in word]
    except KeyError as error_message:
        print("Sorry, ony letters in the alphabet please.")
    else:
        cont = True
        print(code_words)

