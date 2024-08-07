# Season ID

month_input = int(input("Give me the number of any month, from 1 to 12: ")) 

if month_input in [3, 4, 5]:
    season = "Spring"
elif month_input in [6, 7, 8]:
    season = "Summer"
elif month_input in [9, 10, 11]:
    season = "Autum"
elif month_input in [12, 1, 2]:
    season = "Winter"

print(f"The season is {season}")