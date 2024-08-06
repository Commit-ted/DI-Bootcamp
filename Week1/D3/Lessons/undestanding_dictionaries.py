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

# Navigate through the dictionary to access the value of "history"
history_value = sample_dict["class"]["student"]["marks"]["history"]

print(history_value)


