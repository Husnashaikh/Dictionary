dict={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
for i in dict:
    for j in dict:
        if dict[i]>dict[j]:
            dict[i],dict[j]=dict[j],dict[i]
print(dict)

#ASSENDING ODER:
# dict={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# for i in dict:
#     for j in dict:
#         if dict[i]<dict[j]:
#             dict[i],dict[j]=dict[j],dict[i]
# print(dict)