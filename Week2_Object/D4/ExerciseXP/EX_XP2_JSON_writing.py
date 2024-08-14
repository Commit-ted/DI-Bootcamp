import json
import os

# The original JSON string
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Load JSON string into a dictionary
data = json.loads(sampleJson)

# Access the nested "salary" key
salary = data["company"]["employee"]["payable"]["salary"]
print(f"Salary: {salary}")

# Add a new key "birth_date" at the same level as "name"
data["company"]["employee"]["birth_date"] = "1990-01-01"

# Convert the dictionary back to a JSON string
json_string = json.dumps(data, indent=4)

# Get the directory where the current Python script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the file name and create the full path
file_name = "updated_employee.json"
file_path = os.path.join(current_directory, file_name)

# Save the JSON string to a file in the same directory as the script
with open(file_path, "w") as json_file:
    json_file.write(json_string)

print(f"JSON file created at: {file_path}")
