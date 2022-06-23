my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
a=[]
for i in my_dict:
    a.append(my_dict[i])
i=0
b=0
while i<len(a):
    if a[i]>b:
        b=a[i]
    i=i+1
# print(b)    
i=0
c=0
while i<len(a):
    if a[i]>c:
        if a[i]!=b:
            c=a[i]
    i=i+1
# print(c)
i=0
d=0
while i<len(a):
    if a[i]>d:
        if a[i]!=b and a[i]!=c:
            d=a[i]
    i=i+1
# print(d)
a=b,c,d
k=[]
k.append(a)
print(k)
