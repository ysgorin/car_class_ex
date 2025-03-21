# Create a class called Car that has the
# attributes (make, model, year, and color)
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # define a method called describe() which
    # prints out the car's attributes.
    def describe(self):
        print(f'''Make: {self.make}
Model: {self.model}
Year: {self.year}
Color: {self.color}''')

# Create a subclass called ElectricCar
class ElectricCar(Car):
    def __init__(self, make, model, year, color, battery_size):
        super.__init__(make, model, year, color)
        # Add the battery_size attribute to ElectricCar
        self.battery_size = battery_size
    
    # Define a method called describe_battery
    # that prints the battery size
    def describe_battery(self):
        print(f'Battery Size: {self.battery_size}')

# Instantiate two objects of the Car class and
# call the describe() method on both instances
# to print out the details of the cars.
car_1 = Car('Toyota','Corolla',2020,'Red')
car_2 = Car('Honda','Civic',2021,'Blue')
car_3 = ElectricCar('Tesla','Model 3', 2022, 'White', 75)
car_1.describe()
print()
car_2.describe()
print()
car_3.describe()
car_3.describe_battery()