a = [1, 2, 3, 1, 2, 3, 1, 2, 3]
b = []

for i in a:
    if i not in b:
        b.append(i)

print(b)

c = set(a)
print(list())