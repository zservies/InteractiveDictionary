import json
from difflib import get_close_matches

data = json.load(open("data.json"))


# Function that searches the inputted word with the JSON data file.
def input_search(input_word):
    if input_word in data:
        # Prevents errors due to case sensitivity.
        return data[input_word.lower()]
    elif len(get_close_matches(input_word, data.keys())) > 0:
        # Checks for close matches within the data set.
        yn = input("Did you mean: %s? [Y] if yes, [N] if no: " % get_close_matches(input_word, data.keys())[0])
        if yn == "Y".lower():
            return data[get_close_matches(input_word, data.keys())[0]]
        elif yn == "N".lower():
            return "Not found, please try again."
        else:
            return "Must be [Y/N]"

    else:
        return "Not found, please try again."



# Input
word = input("Please enter a word: ")
output = input_search(word)

# Words stored in dataset are in a list.
# Conditionals in function are in string format.
if type(output) == list:
# Loop to iterate list results
    for i in output:
        print(i)
else:
    print(output)