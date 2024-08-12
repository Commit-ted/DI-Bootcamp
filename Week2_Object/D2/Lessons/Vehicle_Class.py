class Vehicle:
    def __init__(self,make, model):
        self.make = make
        self.model = model

    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")

class Car(Vehicle):
    def __init__(self, make, model, number_of_doors):
        super().__init__(make, model)
        self.number_of_doors = number_of_doors

    def open_trunk(self):
        print(f"opening the trunk of {self.make} {self.model}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, has_sidecar = False):
        super().__init__(make, model)
        self.has_sidecar = has_sidecar

    def pop_wheelie(self):
        print(f"the {self.make} {self.model} is popping a wheelie.")

# Create a Car instance and test it
car = Car("Toyota", "Corolla", 4)
car.start()
car.open_trunk()
car.stop()

# Create a Motorcycle instance and test it
motorcycle = Motorcycle("Harley-Davidson", "Street 750")
motorcycle.start()
motorcycle.pop_wheelie()
motorcycle.stop()