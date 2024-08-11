#1
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# cat1 = Cat("Chipi", 1)
# cat2 = Cat("Fluffy", 3)
# cat3 = Cat("Shadow", 7)

# cats = [cat1, cat2, cat3]

# def find_oldest_cat(cats):
#     oldest_cat = max(cats, key=lambda cat: cat.age)
#     return oldest_cat

# oldest_cat = find_oldest_cat(cats)
# print(f"the oldest cat name is {oldest_cat.name}, and is {oldest_cat.age} years old.")

#2
# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height

#     def bark(self):
#         print(f"{self.name} goes woof!")

#     def jump(self):
#         jump_height = self.height * 2
#         print(f"{self.name} jumps {jump_height} cm high")

# davis_dog = Dog("Rex", 50)
# print(f"David's dog name: {davis_dog.name}")
# print(f"David's dog height: {davis_dog.height} cm")
# davis_dog.bark()
# davis_dog.jump()

# sarahs_dog = Dog("Teacup", 20)
# print(f"Sarah's dog name: {sarahs_dog.name}")
# print(f"Sarah's dog height: {sarahs_dog.height} cm")
# sarahs_dog.bark()
# sarahs_dog.jump()

# if davis_dog.height > sarahs_dog.height:
#     print(f"The bigger dog is {davis_dog.name}.")
# else:
#     print(f"The bigger dog is {sarahs_dog.height}.")


#3
# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)

# stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

# # stairway = Song([
# #     "There’s a lady who's sure",
# #     "all that glitters is gold",
# #     "and she’s buying a stairway to heaven"
# # ])

# # Call the sing_me_a_song method to print the lyrics
# stairway.sing_me_a_song()


#4 Zoo
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(f"Animals in {self.name}: {', '.join(self.animals)}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(f"{animal_sold} is not in the zoo.")

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped_animals = {}
        current_letter = ''
        group_id = 1
        
        for animal in sorted_animals:
            if animal[0] != current_letter:
                current_letter = animal[0]
                grouped_animals[group_id] = [animal]
                group_id += 1
            else:
                grouped_animals[group_id - 1].append(animal)
        
        self.grouped_animals = grouped_animals

    def get_groups(self):
        for group_id, group in self.grouped_animals.items():
            print(f"{group_id}: {group}")

# Create the Zoo object
ramat_gan_safari = Zoo("Ramat Gan Safari")

# Adding animals
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Emu")
ramat_gan_safari.add_animal("Eel")

# Display all animals
ramat_gan_safari.get_animals()

# Sell an animal and display the remaining animals
ramat_gan_safari.sell_animal("Bear")
ramat_gan_safari.get_animals()

# Sort animals and display the groups
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
