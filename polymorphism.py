class Vehicle:
    def move(self):
        print("This vehicle moves somehow.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

class Bike(Vehicle):
    def move(self):
        print("Pedaling down the street 🚲")

# Polymorphic behavior
vehicles = [Car(), Plane(), Bike()]

for v in vehicles:
    v.move()

