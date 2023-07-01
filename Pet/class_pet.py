# Create the class instance
class Pet:
    # Create the initializing constructor
    def __init__(self):
            self.__name = ""
            self.__animal_type = ""
            self.__age = 0

    # Create the setter for the attributes
    def set_name(self, name):
        self.__name = name
    
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    # Create the getter for the attibutes
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

# Create the object
pet = Pet()

# Ask for inputs
pet.set_name(input("What is the name of your pet?: "))
pet.set_animal_type(input("What type of animal is your pet?: "))
pet.set_age(input("How old is your pet?(in months): "))

# Print the information
print("\n[PET'S INFORMATION]")
print("Name: ", pet.get_name())
print("Animal Type: ", pet.get_animal_type())
print("Age: ", pet.get_age(), "- month old")