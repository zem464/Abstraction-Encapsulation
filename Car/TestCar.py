# Import class
from class_car import Car

# Create the object
car = Car(2013, 'Hyundai', 0)

# Print the accelerating information 
print("ACCELERATION")
print("\nCar year model: ", car.get_year_model())
print("Car made of: ", car.get_make())
for _ in range(5):
    car.accelerate()
    print("Current speed: ", car.get_speed())

# Print the braking information
print("\nBRAKE")
print("\nCar year model: ", car.get_year_model())
print("Car made of: ", car.get_make())
for _ in range(5):
    car.brake()
    print("Current speed: ", car.get_speed())