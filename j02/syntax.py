# + . - . * . / . % . ** . // . = . == . != . %= ...
# q: how to show anything to user?
# ans:
# print()
# input ---> str
# a = input("user guide...")

print("ali")
# int:
print(1 + 2)
# string
print("1" + "2")
# ---------------------
a = 5
b = 6
c = 2.2
d = "ali"
print("ali")
print(d)


# ex1: write a app to get user firstname and lastname then show fullname

# ans1
firstName = input("enter your firstname: ")
lasttName = input("enter your lastname: ")

# w1
fullName = firstName + " " + lasttName
print("your fullname is: " + fullName)

# w2
print(firstName + " " + lasttName)

# w3
print("your fullname is:", firstName, lasttName) 

# w4 (recommended)
print(f"your fullname is: {firstName} {lasttName}") # f is for format, and {} for placeholder (to insert firstName lasttName")

# w5
print("your fullname is: {} {}".format(firstName, lasttName))

# print has tow usefull atributes
# 1. sep ---> to separate the elements ---> default is " "
# 2. end ---> to end the string ---> default is "\n (new line)"
# 1
print(firstName, lasttName, sep="*", end=" ")
print("welcome")
# 2
print(firstName, lasttName, sep="\n", end="\t")
print("welcome")

# q: how to convert data types?
# ans: use secondary methods
"""
 int() ---> convert to int
 float() ---> convert to float
 str() ---> convert to string
 bool() ---> convert to boolean
 complex() ---> convert to complex
"""

# ex2: write a app to get user name and age then show name and age
# ans2
name = input("enter your name: ")
age = int(input("enter your age: "))
# w1
print("your name is: " + name + " and your age is: " + str(age))
# w2
print("your name is: {} and your age is: {}".format(name, age))
# w3
print(f"your name is: {name} and your age is: {age}")
