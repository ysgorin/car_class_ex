# car_class_ex.py

# Car class with basic attributes and methods
class Car:
    # Class-level attribute
    number_of_wheels = 4

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def describe(self):
        # Prints car details.
        print(f'''Make: {self.make}
Model: {self.model}
Year: {self.year}
Color: {self.color}''')
     
    def is_roadworthy(self):
        # Returns True if the car's year is 2015 or later.
        if self.year >= 2015:
            return True
        else:
            False

# ElectricCar subclass with an additional attribute and method
class ElectricCar(Car):
    def __init__(self, make, model, year, color, battery_size):
        super().__init__(make, model, year, color)
        # Additional attribute for battery size
        self.battery_size = battery_size
    
    def describe_battery(self):
        # Prints battery size.
        print(f'Battery Size: {self.battery_size} kWh')

# Instantiate and describe car objects
cars = [
    Car('Toyota','Corolla',2020,'Red'),
    Car('Honda','Civic',2021,'Blue'),
    ElectricCar('Tesla','Model 3', 2022, 'White', 75)
]

for car in cars:
    car.describe()
    if isinstance(car, ElectricCar):
        car.describe_battery()
    print('-' * 30)

# Modify an attribute and display the update
print('Updating Corolla color to Black...')
setattr(cars[0], 'color', 'Black')
print()
cars[0].describe()
print('-' * 30)

# Display class-level attribute
print(f'Number of Wheels: {Car.number_of_wheels}')
print('-' * 30)

# Check roadworthiness of all cars
for car in cars:
    print(f'Is the {car.model} roadworthy? {car.is_roadworthy()}')