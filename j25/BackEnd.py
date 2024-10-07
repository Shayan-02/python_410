class Person:
    def __init__(mamad, name, age):
        mamad.name = name
        mamad.age = age

    def __str__(reza):
        print(f"{reza.name} {reza.age}")

    def sayHello(self):
        print("Hello my name is ", self.name)


    @staticmethod
    def isAdult():
        print("hi")
    
p1 = Person("John", 36)
p1.sayHello()