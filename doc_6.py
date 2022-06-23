dict={0: 10, 1: 20}
i=0
a=int(input("enter the key"))
b=int(input("enter the value"))
while i<=len(dict):
    dict.update({a:b})
    i=i+1
print(dict)
