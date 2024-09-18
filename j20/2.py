lst2 = [10, 20, 20, 25, 30, 40]

# sum = [i + j for i, j in zip(lst1, lst2)]
sums = sum(lst2)
avg = sums / len(lst2)
miyaneh = (lst2[len(lst2) // 2 - 1] + lst2[len(lst2) // 2]) / 2
enherf = miyaneh - avg

if enherf > 0:
    print(enherf)
else:
    print(enherf * -1)