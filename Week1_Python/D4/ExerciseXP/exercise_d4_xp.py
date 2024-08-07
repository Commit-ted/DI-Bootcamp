#1 Display funtion message
# def display_message():
#     print("I'm learning Python")
# display_message()


#2 What's you favorite Book
# user_input = input("Whats your favorite book")
# def favorite_book(title):
#     print(f"One of your favorite books is {title}.")

# favorite_book(user_input)

#3
# def describe_city(city, country):
#     print(f"The city {city} is the capital of {country}")

# describe_city("Berlin","Germany")

#4
# import random
# def compare_numbers(user_number):
#     if not 1 <= user_number <= 100:
#         print("Please enter a number between 1 and 100.")
#         return
    
#     random_number = random.randint(1, 100)
    
#     if user_number == random_number:
#         print(f"Success! Both numbers are {user_number}.")
#     else:
#         print(f"Fail. Your number: {user_number}, Random number: {random_number}")

# # Ask the user for a number between 1 and 100
# user_number = int(input("Enter a number between 1 and 100: "))

# # Call the function with the user's number
# compare_numbers(user_number)

#5
# def make_shirt(size = "L",text = "I love Python"):
#     print(f"The size os you shirt is {size} and the text in it is {text}.")
# make_shirt()
# make_shirt(size="M")
# make_shirt(size="S", text="balagan!")
# make_shirt(text="Coding Rocks!", size="XL")

#6
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# def show_magicians(names):
#     for name in names:
#         print(name)
# def make_great(names):
#     for i in range(len(names)):
#         names[i] = f"{names[i]} the Great"

# # Call the function make_great to modify the list
# make_great(magician_names)
# # Call the function show_magicians to see that the list has been modified
# show_magicians(magician_names)


#7A
# import random
# def get_random_temp():
#     return random.randint(-10, 40)
# # Test the function to make sure it generates expected results
# for _ in range(1):
#     print(get_random_temp())

#7B
# import random

# def get_random_temp(season):
#     if season == 'winter':
#         return round(random.uniform(-10, 16), 2)
#     elif season == 'spring':
#         return round(random.uniform(0, 23), 2)
#     elif season == 'summer':
#         return round(random.uniform(16, 40), 2)
#     elif season == 'autumn' or season == 'fall':
#         return round(random.uniform(0, 24), 2)
#     else:
#         raise ValueError("Invalid season. Please enter 'winter', 'spring', 'summer', or 'autumn'/'fall'.")

# def main():
#     month_to_season = {
#         1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring',
#         6: 'summer', 7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn',
#         11: 'autumn', 12: 'winter'
#     }
    
#     # Ask the user for the month
#     month = int(input("Please enter the month (1-12): "))
    
#     # Determine the season
#     if 1 <= month <= 12:
#         season = month_to_season[month]
#     else:
#         print("Invalid month. Please enter a value between 1 and 12.")
#         return

#     # Get the temperature
#     temp = get_random_temp(season)
    
#     # Print the temperature
#     print(f"The temperature right now is {temp} degrees Celsius.")
    
#     # Provide advice based on the temperature
#     if temp < 0:
#         print("Brrr, that’s freezing! Wear some extra layers today.")
#     elif 0 <= temp <= 16:
#         print("Quite chilly! Don’t forget your coat.")
#     elif 16 < temp <= 23:
#         print("The weather is moderate. Enjoy your day!")
#     elif 24 <= temp <= 32:
#         print("It's warm outside. Stay hydrated!")
#     elif 32 < temp <= 40:
#         print("It's really hot! Take precautions to avoid heatstroke.")

# # Call the main function
# main()


#8
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def ask_questions(data):
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []

    for item in data:
        user_answer = input(item["question"] + " ")
        if user_answer.strip().lower() == item["answer"].strip().lower():
            correct_answers += 1
        else:
            incorrect_answers += 1
            wrong_answers.append({
                "question": item["question"],
                "user_answer": user_answer,
                "correct_answer": item["answer"]
            })

    return correct_answers, incorrect_answers, wrong_answers

def show_results(correct_answers, incorrect_answers, wrong_answers):
    print(f"\nYou got {correct_answers} correct answers and {incorrect_answers} incorrect answers.")

    if incorrect_answers > 0:
        print("\nHere are the questions you got wrong:")
        for item in wrong_answers:
            print(f"\nQuestion: {item['question']}")
            print(f"Your answer: {item['user_answer']}")
            print(f"Correct answer: {item['correct_answer']}")

    if incorrect_answers > 3:
        print("\nYou had more than 3 wrong answers. Please play again.")

def main():
    correct_answers, incorrect_answers, wrong_answers = ask_questions(data)
    show_results(correct_answers, incorrect_answers, wrong_answers)

    while incorrect_answers > 3:
        print("\nLet's try again!")
        correct_answers, incorrect_answers, wrong_answers = ask_questions(data)
        show_results(correct_answers, incorrect_answers, wrong_answers)

# Run the main function
main()
