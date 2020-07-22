import json

data = json.load(open("data.json"))

def translate(w): # w: local var
    if w in data:
        return data[w]  
    else:    # taking into account bad words
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")    # word: global var

print(translate(word))