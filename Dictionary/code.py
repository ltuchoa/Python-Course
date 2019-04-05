import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s?" %get_close_matches(word, data.keys())[0])
        answer = input("Enter Y if yes, or N if no: ").lower()
        if answer == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif answer == "n":
            return "The word doesn't exist."
        else:
            return "We did'nt understand your entry."
    else:
        return "The word doesn't exist."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
