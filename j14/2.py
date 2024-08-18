class Car:
    def start_engine(self):
        print("The car engine is starting...")


class ElectricCar(Car):
    def start_engine(self):
        print("The electric car is silently starting...")


class HybridCar(Car):
    def start_engine(self):
        print("The hybrid car is starting with both fuel and electric power...")


# استفاده از چندریختی
cars = [Car(), ElectricCar(), HybridCar()]

for car in cars:
    car.start_engine()
