# Import class
from class_pet import Pet

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