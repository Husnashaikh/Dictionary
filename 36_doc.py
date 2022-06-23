a={'key1': 1, 'key2': 3, 'key3': 2}
d={'key1': 1, 'key2': 2}
for a,b in a.items():
    for j,s in d.items():
        if ({a:b})==({j:s}):
            print(a,b,"present in both x and y")





