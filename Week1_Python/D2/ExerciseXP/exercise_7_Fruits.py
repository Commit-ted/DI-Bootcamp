#The usser create a string
favorite_fruits = input("Please enter your favorite fruits (separated by a single space) : ")

favorite_fruits_list = favorite_fruits.split()

extra_fruit = input("Please add the name of any fuit: ")

if extra_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")