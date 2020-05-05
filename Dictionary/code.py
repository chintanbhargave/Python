import json
from difflib import get_close_matches

data = json.load(open("WordDef.json")) # loading data into python data type

def definition(ip):
    ip = ip.lower()  # lowercasing input
    if ip in data:
        return data[ip]
    elif ip.title() in data:  # for the words whose 1st letter is uppercase
        return data[ip.title()]
    elif ip.upper() in data:  # words which are in uppercase
        return data[ip.upper()]
    elif len(get_close_matches(ip, data.keys())) > 0:  # checking if given word has valid definition in the dataset
        val = input("Did you mean {} instead ? Press Y if yes and N if No: ".format(get_close_matches(ip, data.keys())[0])) #suggesting a similar word to user
        if val == 'Y' or val == 'y':
            return data[get_close_matches(ip, data.keys())[0]]   # printing closeest similar word
        elif val == 'N' or val == 'n':
            return "The word doesn't exists "
        else:
            return "Please enter Y or N "
    else:
        return "Word doesn't exists"


word = input("Enter word for its definition: ")

op = definition(word)

if type(op) == list:  # if a word has multiple definitions then printing them on separate lines
    for i in op:
        print(i)
else:
    print(op)   