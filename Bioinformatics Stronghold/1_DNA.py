# Counting DNA Nucleotides

string = input()
A = 0
T = 0
C = 0
G = 0


for x in string:
    if x == "A":
        A+=1
    elif x == "T":
        T+=1
    elif x == "G":
        G+=1
    else:
        C+=1

print (str(A) + " " + str(C) + " " + str(G) + " " + str(T))