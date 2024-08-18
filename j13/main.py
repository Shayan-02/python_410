class Person:
    x = 50
    def __init__(self, name, age, p_id):
        self.name = name
        self.age = age
        self.p_id = p_id
    def sleep(self):
        print(self.name, "is sleeping...")
    def eat(self):
        print(self.name, "eating...")
        
    def say_good_night(self):
        print("good night", self.name, "")

class Student(Person):
    def __init__(self, st_id, avg, degree, major):
        self.st_id = st_id
        self.avg = avg
        self.degree = degree
        self.major = major

s1 = Student(22, 17.5, "bd", "computer")
s2 = Student(21, 16.5, "bd", "math")
s3 = Student(20, 15, "bd", "chemistry")
s1.name = "alireza ahmadi"
print(s1.name)
s1.name = "karim"
s1.sleep()

s2.name = "karim"
s2.say_shab_bekheir()