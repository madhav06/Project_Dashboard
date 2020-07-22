import json

data = json.load(open("data.json"))

def translate(w):    # w: local var
    w = w.lower() 
    if w in data:
        return data[w]  
    elif len(get_close_matches(w, data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(w, data.keys())[0]
    else:    # taking into account bad words
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")    # word: global var

print(translate(word))