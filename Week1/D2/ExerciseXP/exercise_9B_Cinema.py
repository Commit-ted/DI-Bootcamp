# List of teenagers' names
teenagers = ["Alice", "Bob", "Charlie", "David", "Eva"]

# Ask each teenager for their age
allowed_teenagers = []

for teen in teenagers:
    try:
        age = int(input(f"Enter the age of {teen}: ").strip())
        if 16 <= age <= 21:
            print(f"{teen} is not permitted to watch the movie and will be removed from the list.")
        else:
            allowed_teenagers.append(teen)
    except ValueError:
        print(f"Invalid age input for {teen}. They will be removed from the list.")

# Print the final list of teenagers who are allowed to watch the movie
print("\nFinal list of teenagers allowed to watch the movie:")
print(allowed_teenagers)
