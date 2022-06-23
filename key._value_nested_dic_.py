a={"a":1,"b":{"c":4,"d":3}}
for i in a:
    print(i)
    if type(a[i])!=int:
        for j in a[i]:
            print(j)


a={"a":1,"b":{"c":4,"d":3}}
for i in a:
    if type (a[i])==dict:
        for j in a[i]:
            print(a[i][j])
    else:
        print(a[i])

