import json

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

# Save the updated dictionary as a JSON file
with open("updated_employee.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
