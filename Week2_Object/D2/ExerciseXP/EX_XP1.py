#1-Cats
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# # Create instances of each cat breed
# bengal = Bengal("Bengal", 2)
# chartreux = Chartreux("Chartreux", 3)
# siamese = Siamese("Siamese", 1)

# # Create a list of all the cats
# all_cats = [bengal, chartreux, siamese]

# # Create an instance of Pets with all_cats
# sara_pets = Pets(all_cats)

# # Take all the cats for a walk
# sara_pets.walk()


# #2 DOGS
# class Dog():
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight

#     def bark(self):
#         return f"{self.name} is barking."

#     def run_speed(self):
#         return (self.weight / self.age) * 10
    
#     def fight(self, other_dog):
#         self_score = self.run_speed() * self.weight
#         other_dog_score = other_dog.run_speed() * other_dog.weight 
#         if self_score > other_dog_score:
#             return f"{self.name} wins the fight against {other_dog.name}."
#         elif self_score < other_dog_score:
#             return f"{other_dog.name} wins the fight against {self.name}."
#         else:
#             return "It's a tie!"
        
# dog1 = Dog("Timi", 5, 17)
# dog2 = Dog("Bella", 3, 15)
# dog3 = Dog("Max", 7, 25)


# print(dog1.bark())
# print(dog2.bark())
# print(dog3.bark())

# print(f"{dog1.name}'s running speed: {dog1.run_speed()}")
# print(f"{dog2.name}'s running speed: {dog2.run_speed()}")
# print(f"{dog3.name}'s running speed: {dog3.run_speed()}")

# print(dog1.fight(dog2))
# print(dog2.fight(dog3))
# print(dog1.fight(dog3))