import json
from difflib import get_close_matches
data = json.load(open("076 data.json"))
def trans(w):
    w = w.lower()
    if w in data:
            return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
            yn = input("Did you mean %s instead? Enter Y if yes and N if no: " % get_close_matches(w, data.keys())[0])
            if yn == "Y":
               return data[get_close_matches(w, data.keys())[0]]
            elif yn =="N":
                 return "The word doesn't exist. Please double check it."
            else:
             return "We didn't understand your entry."
    else:
         return "The word doesn't exist. Please double check it."

word = input("Enter a word:")
output = trans(word)

if type(output) == list:
    for item in output:
        print(item)
    else:
        print(output)

