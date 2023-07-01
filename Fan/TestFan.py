# Import the class fan
from class_fan import Fan

# Construct a program for the functions for the fan1 and fan2
class TestFan(Fan):
    def main(self):
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

# Close the program by creating an instance method
TestFan().main()