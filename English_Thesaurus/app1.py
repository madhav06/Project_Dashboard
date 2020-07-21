import json

data = json.load(open("data.json"))

def translate(w):
    return data[w]

#global variable
word = input("Enter word: ")

print(translate(word))