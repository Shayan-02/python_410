lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 4, 9, 16, 25]
d = {}

for i in range(min(len(lst1), len(lst2))):
    d[lst1[i]] = lst2[i]

print(d)

print(dict(zip(lst1, lst2)))
