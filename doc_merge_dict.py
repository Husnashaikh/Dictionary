dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={}
i=0
while i<len(dic1):
    dic3.update(dic1)
    dic3.update(dic2)
    i=i+1
print(dic3)