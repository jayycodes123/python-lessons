class Dog:
    species = "Canine"  # Class attribute
    state = "alive"
    def __init__(self, name, age, colour):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
        self.colour = colour
dog1 = Dog("Buddy", 3 , "brown")  # Create an instance of Dog
dog2 = Dog("Charlie", 5 , "black")  # Create another instance of Dog

print(dog1.name, dog1.age, dog1.species, dog1.colour)  # Access instance and class attributes
print(dog2.name, dog2.age, dog2.species, dog2.colour)  # Access instance and class attributes
print(Dog.species)  # Access class attribute directly
print(Dog.state)

Dog.state = "dead"
print(Dog.state)
