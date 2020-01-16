# Rabbits and Recurrence Relations

n = int(input())
k = int(input())

rabbits = [1, 1]

for x in range (2, n):
    rabbits.append(3*(rabbits[x-2])+rabbits[x-1])

print(rabbits[-1])