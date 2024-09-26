import pandas as pd
import matplotlib.pyplot as plt

# File path to your Excel file
file_path = "/Users/manuel/Desktop/DI-Bootcamp/Week7_WebScrapping/D5/ExerciseXP/EX_4_productSales.xlsx"

# Read data from the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Manipulate the data: group by 'product' and sum the 'sales' for each product
grouped_data = df.groupby('product')['sales'].sum().reset_index()

# File path to save the new Excel file
output_file = '/Users/manuel/Desktop/DI-Bootcamp/Week7_WebScrapping/D5/ExerciseXP/sales_report.xlsx'

# Export the grouped data to a new Excel file using pandas' to_excel() function
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    grouped_data.to_excel(writer, index=False, sheet_name='Product Sales Summary')

print(f"Sales report has been successfully saved to {output_file}")
