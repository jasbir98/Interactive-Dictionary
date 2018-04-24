import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        check = get_close_matches(w, data.keys())[0]
        opt = input("Did you mean %s instead? Enter Y for yes, or N if no. " % check).lower()
        if opt == 'y':
            return data[check]
        elif opt == 'n':
            return "The word doesn't exist. Please check again!"
        else:
            return "Please Enter a valid Key!"
    else:
        return "The word doesn't exist. Please check again!"

word = input("Enter a Word: ")

getlist = translate(word)
if type(getlist) == list:
    for i in range(len(getlist)):
        print(i+1,". ",getlist[i])
else:
    print(getlist)