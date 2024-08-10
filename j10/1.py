d = 9
def sums(a, b):
    global d, c
    d = 10
    c = a + b
    return c


num1 = int(input("number1: "))
num2 = int(input("number2: "))
print(sums(num1, num2))
print(c)

d *= 10
print(d)