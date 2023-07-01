# Import class
from class_fan import Fan

# Create a defining function for the objects
def TestFan():
    fan1 = Fan(Fan.fast, 10, "Yellow", True)
    fan2 = Fan(Fan.medium, 5, "Blue", False)

    # Display fan1
    print("[First Fan]")
    print("Speed: ", fan1.get_speed())
    print("Radius: ", fan1.get_radius())
    print("Color: ", fan1.get_color())
    print("On: ", fan1.get_fan_on())

    # Display fan2
    print("[Second Fan]")
    print("Speed: ", fan2.get_speed())
    print("Radius: ", fan2.get_radius())
    print("Color: ", fan2.get_color())
    print("On: ", fan2.get_fan_on())

# Call the main function
TestFan()