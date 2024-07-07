n1 = int(input("enter first number: "))
n2 = int(input("enter first number: "))
n3 = int(input("enter first number: "))

if n1 > n2 and n2 > n3:
    print(f"max is {n1}, mid is {n2} and min is {n3}")
elif n2 > n1 and n1 > n3:
    print(f"max is {n2}, mid is {n1} and min is {n3}")
elif n3 > n1 and n1 > n2:
    print(f"max is {n3}, mid is {n1} and min is {n2}")
elif n1 > n3 and n3 > n2:
    print(f"max is {n1}, mid is {n3} and min is {n2}")
elif n2 > n3 and n3 > n1:
    print(f"max is {n2}, mid is {n3} and min is {n1}")
elif n3 > n2 and n2 > n1:
    print(f"max is {n3}, mid is {n2} and min is {n1}")
elif n1 == n2 > n3:
    print(f"max is {n1} and min is {n3}")
elif n1 == n3 > n2:
    print(f"max is {n1} and min is {n2}")
elif n2 == n3 > n1:
    print(f"max is {n2} and min is {n1}")
else:
    print("all are equal")