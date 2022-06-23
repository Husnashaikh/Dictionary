dict={1:20,2:10,3:40}
dict1=[]
for i in dict:
    dict1.append(dict[i])
i=0
sum=0
while i<len(dict1):
    sum=sum+dict1[i]
    i=i+1
print(sum)
