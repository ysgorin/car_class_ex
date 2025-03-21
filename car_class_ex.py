# Create a class called Car that has the attributes (make, model, year, and color)
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # define a method called describe() which prints out the car's attributes.
    def describe(self):
        print(f'''Make: {self.make}
Model: {self.model}
Year: {self.year}
Color: {self.color}''')

# Instantiate two objects of the Car class and call the describe() method on both instances to print out the details of the cars.
car_1 = Car('Toyota','Corolla',2020,'Red')
car_2 = Car('Honda','Civic',2021,'Blue')
car_1.describe()
car_2.describe()