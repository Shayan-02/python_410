from pprint import *
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7 ,8],
    [9, 10, 11, 12]
]
pprint(matrix, width=20)

print()

transposted = [[row[i] for row in matrix] for i in range(4)]
pprint(transposted, width= 20)

print()

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

z = list(zip(x, y))
print(z)

pprint([list(i) for i in list(zip(*matrix))], width = 20)

