def mult(x):
    for i in range(1, x + 1):
        for j in range(1, x + 1):
            print(i * j, end = "\t")
        print("\n")

num = int(input("enter a number: "))
mult(num)