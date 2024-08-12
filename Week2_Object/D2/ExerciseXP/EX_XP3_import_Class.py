# Importing the Dog class
from EX_XP2_Class_dog import Dog
import random

# Define the PetDog class that inherits from Dog
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False  # New attribute to track if the dog is trained

    def train(self):
        print(self.bark())  # Prints the dog's bark
        self.trained = True  # Switch the trained attribute to True

    def play(self, *args):
        dog_names = ', '.join([dog.name for dog in args])
        print(f"{self.name}, {dog_names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet and can't do a trick.")

# Test the PetDog class
dog1 = PetDog("Rex", 5, 20)
dog2 = PetDog("Bella", 3, 15)
dog3 = PetDog("Max", 7, 25)

# Train Rex and have him do a trick
dog1.train()
dog1.do_a_trick()

# Have the dogs play together
dog1.play(dog2, dog3)

# Try having an untrained dog do a trick
dog2.do_a_trick()
# Train Bella
dog2.train()
dog2.do_a_trick()
