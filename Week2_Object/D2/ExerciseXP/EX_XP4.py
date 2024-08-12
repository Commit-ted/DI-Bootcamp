#Family
class Family():
    def __init__(self, last_name, members=None):
        self.members = members if members is not None else []
        self.last_name = last_name

    def born(self, **kwargs):
        # Add the new member to the family
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family on the birth of {kwargs['name']}!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False
    
    def family_presentation(self):
        print(f"The {self.last_name} family members:")
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Is Child: {member['is_child']}")

# Initial members of the family
initial_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

# Create an instance of the Family class
my_family = Family(last_name="Kizer", members=initial_members)

# Add a new child to the family
my_family.born(name="John", age=0, gender="Male", is_child=True)
my_family.born(name="Andres", age=40, gender="Male", is_child=False)

# Check if Michael is over 18
print(f"Is Michael over 18? {my_family.is_18('Michael')}")

# Check if John is over 18
print(f"Is John over 18? {my_family.is_18('John')}")

# Print the family presentation
my_family.family_presentation()

#5
class TheIncredibles(Family):
    def __init__(self, last_name, members=None):
        super().__init__(last_name, members)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{member['incredible_name']}'s power is {member['power']}")
                else:
                    raise Exception(f"{name} is not over 18 years old and cannot use their power!")
                return
        raise Exception(f"No member named {name} found in the family.")

    def incredible_presentation(self):
        print("*Here is our powerful family*")
        super().family_presentation()

# Create an instance of TheIncredibles class
incredibles_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

incredibles_family = TheIncredibles(last_name="Incredibles", members=incredibles_members)

# Call the incredible_presentation method
incredibles_family.incredible_presentation()

# Use the born method to add Baby Jack with the "Unknown Power"
incredibles_family.born(name="Baby Jack", age=0, gender="Male", is_child=True, power="Unknown Power", incredible_name="BabyJack")

# Call the incredible_presentation method again
incredibles_family.incredible_presentation()

# Attempt to use powers
try:
    incredibles_family.use_power("Michael")
    incredibles_family.use_power("Sarah")
    incredibles_family.use_power("Baby Jack")  # Should raise an exception
except Exception as e:
    print(e)
