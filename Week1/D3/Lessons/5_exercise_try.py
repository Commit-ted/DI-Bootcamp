user_input = input("Please provide a number: or Q to quit ")

#Use try-except to handle errors/exeptions
numbers = []
while True:
  if user_input == "Q":
    break
    print("You quit")
  try:
    number =int(user_input)
    numbers.append(number)
    print(f"Usser's input is: {number}")
  except ValueError:
    print("Invalid input please try again") 

  print(numbers)

print("You quit")