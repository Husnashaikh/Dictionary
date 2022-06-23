dict=[{"first":"1"}, {"second": "2"}, {"third": "1"}, 
{"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}
]
a={}
i=0
while i<len(dict):
    if dict[i] in dict:
        a.update(dict[i])
    i=i+1
j=0
b=[]
for j in a:
    b.append(a[j])
k=0
c=[]
while k<len(a):
    if b[k] not in c:
        c.append(b[k])
    k=k+1
print(c)