# q = input("start? ")

# while "q" == "y":
while "y" in (q:= input("? ").lower()):
    x = int(input("enter a number: "))
    print(x ** 2)
    # q = input("continue? ")
