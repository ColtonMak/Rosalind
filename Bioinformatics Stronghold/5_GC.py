# Computing GC Content

fasta = open("rosalind_gc.txt", "r")

id = []
gc = []
GCCount = 0
totalCount = 0
currentString = ""
lines = fasta.readlines()


for x in lines:

    if x[0] == ">":
        id.append(x[1:])      
        if currentString != "":

            for symbol in currentString:
                if symbol == "C":
                    GCCount += 1
                    totalCount += 1
                elif symbol == "G":
                    GCCount += 1
                    totalCount +=1
                elif symbol == "T":
                    totalCount +=1
                elif symbol == "A":
                    totalCount += 1
            gc.append((GCCount/totalCount)*100)

        currentString = ""
        GCCount = 0
        totalCount = 0

    else:
        currentString += x

id.pop(-1)

highestID = id[0]
highestGC = gc[0]

for i in gc:
    if i > highestGC:
        highestGC = i
        highestID = id[gc.index(i)]

print(highestID)
print(highestGC)