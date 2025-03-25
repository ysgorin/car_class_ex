# Car and ElectricCar Classes in Python
### Overview
A simple Python project demonstrating <b>Object-Oriented Programming (OOP)</b> concepts such as <b>classes, inheritance, attributes, and methods</b>.

### Features
* <b>`Car` Class:</b> Represents a general car with attributes like `make`, `model`, `year`, and `color`.
* <b>`ElectricCar` Subclass:</b> Inherits from `Car` and adds a `battery_size` attribute.
* <b>Methods:</b>
    * `describe()`: Prints car details.
    * `is_roadworthy()`: Checks if a car's year is 2015 or later.
    * `describe_battery()`: Prints the battery size (for `ElectricCar` only).

### Sample Output
```sh
Make: Toyota  
Model: Corolla
Year: 2020    
Color: Red    
------------------------------    
Make: Honda
Model: Civic
Year: 2021
Color: Blue
------------------------------    
Make: Tesla
Model: Model 3
Year: 2022
Color: White
Battery Size: 75 kWh
------------------------------    
Updating Corolla color to Black...

Make: Toyota
Model: Corolla
Year: 2020
Color: Black
------------------------------    
Number of Wheels: 4
------------------------------
Is the Corolla roadworthy? True
Is the Civic roadworthy? True
Is the Model 3 roadworthy? True
```