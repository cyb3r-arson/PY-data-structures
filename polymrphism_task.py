# Base class for vehicles
class Vehicle:
    def move(self):
        pass

# Derived class: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Derived class: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Base class for animals
class Animal:
    def move(self):
        pass

# Derived class: Dog
class Dog(Animal):
    def move(self):
        print("Running 🐕")

# Derived class: Bird
class Bird(Animal):
    def move(self):
        print("Flying 🐦")

# Create instances of vehicles and animals
car = Car()
plane = Plane()
dog = Dog()
bird = Bird()

# Polymorphism in action: Call move() on different objects
vehicles = [car, plane]
animals = [dog, bird]

for vehicle in vehicles:
    vehicle.move()

for animal in animals:
    animal.move()
