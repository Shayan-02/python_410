a = (1, 2, 3)
b = [1, 2, 3]

c = list(a)
c[1] = "ali"
a = tuple(c)
print(a)