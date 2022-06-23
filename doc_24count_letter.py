k="w3resource"
i=0
a=[]
while i<len(k):
    j=0
    b=[]
    coun=0
    while j<len(k):
        if k[i] in k:
            if k[i]==k[j]:
                coun=coun+1
        j=j+1
    b.append(k[i])
    b.append(coun)
    if b not in a:
        a.append(b)
    i=i+1
print(a)





















# Q2. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

