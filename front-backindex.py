a=["a","b","c","d","e","f"]
b=["g","h","i","j","k",'l']
i=0
c={}
while i<len(a):
    h=a[i]+b[-i]
    c.update({i:h})
    i=i+1
print(c)
