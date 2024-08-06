#Create a dictonary name brand

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# Print the brand dictionary to verify
#print(brand)

#3. Change the number of stores to 2 - Update method
brand["number_stores"] = 2
#print(brand)

#4 Create a sentence that explains who Zara's clients are
clients =  ", ".join(brand["type_of_clothes"])
sentence = f"Zara's clients are {clients}."
# Print the sentence
#print(sentence)

#5
brand["country_creation"] = "Spain"
# Print the updated brand dictionary to verify the change
#print(brand)

#6
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
#print(brand)

#7
del brand["creation_date"]

#8
last_competitor = brand["international_competitors"] [-1]
print("The last international competitor is:", last_competitor)

#9 colors in US
colors_us = brand["major_color"] ["US"]
print("The major clothes colors in the US are:", colors_us)

#10 len - check/count the ammount of entries
num_pairs = len(brand)
print("The number of key-value pairs in the dictionary is:", num_pairs)

#11 Print the keys of the dictionary
print("The keys of the dictionary are:")
for key in brand.keys():
    print(key)

#12 Anothe dictoriory
more_on_zara = {
    'creation_date': 1975, 
    'number_stores': 10000
}

#13 update - the creation date rewrite the old one
brand.update(more_on_zara)
print(brand)

#13 len - here double check
num_pairs = len(brand)
print("The number of key-value pairs in the dictionary is:", num_pairs)

#14  Print the value of the key number_stores After updating
print("The value of the key 'number_stores' is:", brand["number_stores"])
