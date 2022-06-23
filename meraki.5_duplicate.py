dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
dict={}
for x,y in dic.items():
    if x not in dict:
        dict.update({x:y})
print(dict)