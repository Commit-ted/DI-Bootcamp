# Option 1: Importing the entire module
# import func
# func.sum_two_numbers(3, 5)

# Option 2: Importing the function directly
# from func import sum_two_numbers
# sum_two_numbers(8, 5)

# Option 3: Importing with an alias
# from func import sum_two_numbers as sum_fn
# sum_fn(10, 5)

# Option 4: Importing the module with an alias
import func as f
f.sum_two_numbers(15, 5)