import requests
import sqlite3
import random

# Fetch all countries data from the REST Countries API
response = requests.get('https://restcountries.com/v3.1/all')
if response.status_code != 200:
    print('Failed to retrieve data from the REST Countries API')
    exit()

countries = response.json()

# Select 10 random countries
random_countries = random.sample(countries, 10)

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('countries.db')
cursor = conn.cursor()

# Create the table with the specified attributes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        name TEXT,
        capital TEXT,
        flag TEXT,
        subregion TEXT,
        population INTEGER
    )
''')

# Insert data into the table
for country in random_countries:
    name = country.get('name', {}).get('common', 'N/A')
    capital_list = country.get('capital', ['N/A'])
    capital = capital_list[0] if capital_list else 'N/A'
    flag = country.get('flags', {}).get('png', 'N/A')
    subregion = country.get('subregion', 'N/A')
    population = country.get('population', 0)

    cursor.execute('''
        INSERT INTO countries (name, capital, flag, subregion, population)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, capital, flag, subregion, population))

# Commit the transaction and close the connection
conn.commit()
conn.close()

print("Data for 10 random countries has been written to the database.")
