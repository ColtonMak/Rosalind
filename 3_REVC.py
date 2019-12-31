# Complementing a Strand of DNA

string = input()[::-1]
newstring = ""

for x in string:
    if x == "A":
        newstring += "T"
    elif x == "T":
        newstring += "A"
    elif x == "C":
        newstring += "G"
    else:
        newstring += "C"
print(newstring)