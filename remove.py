a={"a 001":["maths"],"s 002":["maths"]}
c={}
for key in a.keys():
    str=""
    for i in key:
        if i!=" ":
            str+=i
        b=str
    print(b)
    c.update({b:a})
    print(c)