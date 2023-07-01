# Create class fan
class Fan:
    # Create the constants
    slow = 1
    medium = 2
    fast = 3

    # Initialize the needed data field
    def __init__(self, speed, radius, color, fan_on):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__fan_on = fan_on

    # Create the getters
    def get_speed(self):
        return self.__speed
    
    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color
    
    def get_fan_on(self):
        return self.__fan_on

# Create the setters

# Create methods for the default values