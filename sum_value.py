a={"a":2,"b":-19,"c":77}
c=[]
for i in a:
    c.append(a[i])
print(c)
j=0
r=0
while j<len(c):
    r=r+c[j]
    j=j+1
print(r)
