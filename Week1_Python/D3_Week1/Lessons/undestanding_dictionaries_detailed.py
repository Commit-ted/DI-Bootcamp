# Access the value of key "history"
sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

# Print the entire dictionary
print(sample_dict)

# Access and print keys at the top level
print(sample_dict.keys())

# Access the nested "class" dictionary
class_key_vals = sample_dict["class"]
print(class_key_vals.keys())

# Access the nested "student" dictionary
student_key_vals = class_key_vals["student"]
print(student_key_vals.keys())

# Access the nested "marks" dictionary
mark_key_vals = student_key_vals["marks"]
print(mark_key_vals.keys())

# Access the "history" value
history_value = mark_key_vals["history"]
print(history_value)
