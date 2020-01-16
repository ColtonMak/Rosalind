# Finding a motif in DNA

# string
s = input()
# substring
t = input()


i = 1
while (i < (len(s)-len(t)+2)):
    fragment = s[i-1:i+len(t)-1]
    if fragment == t:
        print(i)
    i = i + 1
