# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# p1  = Person("hassan", 36)
# p2 = Person("ali", 35)
# p3 = Person("reza", 20)
# p4 = Person("mohsen", 40)
# p5 = Person("mohammad", 45)
# p6 = Person("hossein", 50)
#
# print(p1.name)
# print(p1.age)
# print(p2.name)
#
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def __str__(self):
#     return f"{self.name}({self.age})"
#
# p1 = Person("John", 36)
#
# print(p1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
p1.myfunc()