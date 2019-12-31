# Counting Point Mutations

str1 = list(input())
str2 = list(input())
hamm = 0

for x in range(0, len(str1)):
    if str1[x] != str2[x]:
        hamm += 1

print(hamm)