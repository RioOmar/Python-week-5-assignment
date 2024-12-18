# Base class (optional for structure)
class Mover:
    def move(self):
        pass  # Placeholder for polymorphic behavior

# Vehicle classes
class Car(Mover):
    def move(self):
        print("Driving 🚗")

class Plane(Mover):
    def move(self):
        print("Flying ✈️")

class Boat(Mover):
    def move(self):
        print("Sailing 🚤")

# Animal classes
class Dog(Mover):
    def move(self):
        print("Running 🐕")

class Bird(Mover):
    def move(self):
        print("Flying 🐦")

class Fish(Mover):
    def move(self):
        print("Swimming 🐠")

# Polymorphic Function
def make_it_move(movers):
    for mover in movers:
        mover.move()

# Create objects
car = Car()
plane = Plane()
boat = Boat()
dog = Dog()
bird = Bird()
fish = Fish()

# List of movers
movers = [car, plane, boat, dog, bird, fish]

# Call the polymorphic function
print("The movers are in action!\n")
make_it_move(movers)
