import json


data = json.load(open("./data/data.json"))


def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    
    else:
        print("pugger your paw steps on wrong keys")


   

word = input("Enter the word you want to search:")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)