class Car:
    def __init__(self, make, model, year):
        self.m = make  # برند ماشین
        self.model = model  # مدل ماشین
        self.year = year  # سال تولید ماشین

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model} engine has started!")

    def stop_engine(self):
        print(f"The {self.year} {self.make} {self.model} engine has stopped.")


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size): # تابع سازنده
        super().__init__(make, model, year)
        self.battery_size = battery_size  # اندازه باتری

    def charge_battery(self):
        print(f"The {self.battery_size}-kWh battery is now fully charged!")



my_electric_car = ElectricCar("Tesla", "Model S", 2022, 100)


my_electric_car.start_engine()
my_electric_car.charge_battery()


my_car = Car("Toyota", "Camry", 2020)


my_car.start_engine()
my_car.stop_engine()
