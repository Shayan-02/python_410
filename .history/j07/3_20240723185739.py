a = [1, 2, 3]
b = [3, 4, 5]
c = []
print(list(set(a) - set(b)))
print(list(set(b) - set(a)))


for i in a:
    if i in b:
        print(i)
c.append(i)
print(c)