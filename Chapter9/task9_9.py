class Battery:
    def __init__(self, battery_size):
        self.range = 10000
        self.battery_size = battery_size

    def describe_battery(self):
        print('battery_size:' + str(self.battery_size) + ' range:' + str(self.range))

    def get_range(self):
        self.range = self.battery_size * 100

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        print(long_name)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(60)


car = ElectricCar('BMW', 'SUV', 2020)
car.battery.get_range()
car.battery.describe_battery()
car.battery.upgrade_battery()
car.battery.get_range() 
car.battery.describe_battery()
