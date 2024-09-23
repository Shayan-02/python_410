num1 = int(input("enter a number: "))
op = input("enter an operator: ")
num2 = int(input("enter another number: "))


if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print("can't divide by zero")
else:
    print("invalid operator")


print("edameh")