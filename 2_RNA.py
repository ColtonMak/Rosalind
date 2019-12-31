# Transcribing DNA into RNA

string = input()
newstring = ""

for x in string:
    if x == "T":
        newstring += "U"
    else:
        newstring += x

print (newstring)