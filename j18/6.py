class Test1:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
    
    def add(a, b):
        return Test1(a + b)

    # def add(self, other):
    #     return Test1(self.a + other.a, self.b + other.b)
    

a = Test1(10, 20)
b = Test1(30, 40)

