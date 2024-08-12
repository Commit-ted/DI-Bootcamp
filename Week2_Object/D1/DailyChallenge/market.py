#Macdonnals farm
class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        farm_info = f"{self.name}'s farm\n"
        for animal, count in self.animals.items():
            farm_info += f"{animal} : {count}\n"
        farm_info += "\n    E-I-E-I-0!\n"
        return farm_info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        pluralized_animals = [animal + 's' if self.animals[animal] > 1 else animal for animal in animal_types]
        return f"{self.name}’s farm has " + ', '.join(pluralized_animals[:-1]) + f" and {pluralized_animals[-1]}."

# Create the farm object
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

# Print the farm information
print(macdonald.get_info())

# Get the sorted list of animal types
print(macdonald.get_animal_types())

# Print the short information about the farm
print(macdonald.get_short_info())
