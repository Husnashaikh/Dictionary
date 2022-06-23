k="MISSISSIPPI"
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