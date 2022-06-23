dict={1:5,2:2,3:4}
dict1=[]
for i in dict:
    dict1.append(dict[i])
i=0
pro=1
while i<len(dict1):
    pro=pro*dict1[i]
    i=i+1
print(pro)