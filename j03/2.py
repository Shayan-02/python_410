a = int(input("enter a number: "))

n1 = a % 10
n2 = a // 10

print("reverse:", n1, n2, sep = "")
print("sum:", (int(str(n1) + str(n2)) + a))
print("sum of digits:", n1 + n2)