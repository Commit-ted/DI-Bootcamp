import os
import glob
import pandas as pd
from datetime import datetime

# Step 1: Define the directory containing the CSV files
csv_folder = '/Users/manuel/Desktop/Hackaton Jean Pierre/Data/Organic/Organic_3months'

# Step 2: Get a list of all CSV files in the directory
csv_files = glob.glob(os.path.join(csv_folder, '*.csv'))

# Step 3: Extract dates from filenames and sort the files
def extract_start_date(filename):
    # Get the base name without the path
    base_name = os.path.basename(filename)
    # Split the filename to get the start date part
    start_date_str = base_name.split('_')[0]  # 'Apr-01-2022'
    # Convert to datetime object
    start_date = datetime.strptime(start_date_str, '%b-%d-%Y')
    return start_date

# Create a list of tuples (filename, start_date)
files_with_dates = [(file, extract_start_date(file)) for file in csv_files]

# Sort the list of files based on the start date
sorted_files_with_dates = sorted(files_with_dates, key=lambda x: x[1])

# Extract the sorted list of filenames
sorted_csv_files = [file for file, date in sorted_files_with_dates]

# Step 4: Initialize an empty list to hold DataFrames
df_list = []

# Step 5: Loop through the sorted CSV files and read them into DataFrames
for file in sorted_csv_files:
    df = pd.read_csv(file)
    # Check if 'Publish time' column exists
    if 'Publish time' in df.columns:
        # Convert 'Publish time' to datetime format
        df['Publish time'] = pd.to_datetime(df['Publish time'], format='%m/%d/%Y %H:%M')
    else:
        print(f"Warning: 'Publish time' column not found in file {file}. Filling with NaT.")
        # Add 'Publish time' column with NaT (Not a Time)
        df['Publish time'] = pd.NaT
    # Append the DataFrame to the list
    df_list.append(df)

# Step 6: Concatenate all DataFrames into one
combined_df = pd.concat(df_list, ignore_index=True)

# Step 7: Sort the combined DataFrame by 'Publish time' column
combined_df.sort_values(by='Publish time', inplace=True)

# Step 8: Save the combined DataFrame to a new CSV file
output_file = '/Users/manuel/Desktop/Hackaton Jean Pierre/Data/Organic/combined_csv.csv'
combined_df.to_csv(output_file, index=False)

print(f"Combined {len(df_list)} CSV files into {output_file}")
