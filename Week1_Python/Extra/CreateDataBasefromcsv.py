import pandas as pd
import sqlite3
import os

# Step 1: Load the CSV file into a DataFrame
csv_file_path = '/Users/manuel/Desktop/DI-Bootcamp/Week10_AdvanceSQL/extra/laptopData.csv'
data = pd.read_csv(csv_file_path)

# Step 2: Generate the path for the .db file with the same name
db_file_path = os.path.splitext(csv_file_path)[0] + '.db'

# Step 3: Connect to SQLite database (creates a new file if it doesn’t exist)
conn = sqlite3.connect(db_file_path)

# Step 4: Write the DataFrame to the SQLite database
table_name = 'laptop_data'  # Define a table name for the .db file
data.to_sql(table_name, conn, if_exists='replace', index=False)

# Step 5: Close the database connection
conn.close()

print(f"CSV data successfully transformed into {db_file_path}")
