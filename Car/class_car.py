# Create the class for the car
class Car:
    # Initialize the needed attributes
    def __init__(self, year_model, make, speed):
            self.__year_model = year_model
            self.__make = make
            self.__speed = speed

    # Create the method for acceleration
    def accelerate(self):
            self.__speed += 5

    # Create the method for braking
    def brake(self):
            self.__speed -= 5
            if self.__speed < 0:
                self.__speed = 0

    # Create the getter for the attributes
    def get_year_model(self):
        return self.__year_model
    
    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

# Create the object
car = Car(2013, 'Hyundai', 0)

# Create the accelerating information 
print("ACCELERATION")
print("\nCar year model: ", car.get_year_model())
print("Car made of: ", car.get_make())
for _ in range(5):
    car.accelerate()
    print("Current speed: ", car.get_speed())

# Create the braking information