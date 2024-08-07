# user's word : "ttiiitllleeee" ➞ "title"

#             SET - {"ppoeemm"} -> "oemp", "oepm"... sets are not ordered
#             LIST - [] -> loop through chars in word and check if character is inside
#                           the list - if it is DONT add it to the list
#                           otherwise add it to the list
#                           -> ["p","o","e","m"] ... wont work since the characters can
#                           repeat themselves like it title (2 t's)


#               "ttiii" 
#                  i      
#                i = 0
#               ["t", "i"] 
#               current_char = word[i] # "t"
#               while i < len("ttiii"):
#
#                   if string[i] != current_char:
#                      ["t",].append("i")
#                      current_char = string[i] # "i"
#                   i += 1
#              
#               