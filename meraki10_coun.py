dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
coun=1
a=[]
for i in dict1:
    a.append(dict1[i])
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        coun=coun+j
        j=j+1
    i=i+1
print(coun)