class Battery:
    def __init__(self,battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = f"Estimated range on a full charge: {range} miles."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

class electricCAR:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()


my_car = electricCAR("Tesla", "ModelY","2024")

my_car.battery.describe_battery()
my_car.battery.get_range()

my_car.battery.upgrade_battery()

my_car.battery.describe_battery()
my_car.battery.get_range()

