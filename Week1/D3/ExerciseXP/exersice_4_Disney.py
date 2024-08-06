# Play arround the dictionary
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

#1 Map each user name to its original index in the users list.
disney_ussers_A = {}
for index, user in enumerate(users):
    disney_ussers_A[user] = index

print(disney_ussers_A)
#2 Map each index to the corresponding user name in the users list.
disney_ussers_B = {}
for index, user in enumerate(users):
    disney_ussers_B[index] = user
print(disney_ussers_B)

#3 Map each user name to its index in the alphabetically sorted users list
disney_ussers_C = {user: index for index, user in enumerate(sorted(users))}
print(disney_ussers_C)

#1.2 The Characters Whose Names Contain the Letter "i"
disney_character_with_letter_i = {}
for index, user in enumerate(users):
    if 'i' in user:
        disney_character_with_letter_i[user] = index 
print(disney_character_with_letter_i)

#1.3 The Characters Whose Names Start with the Letter "m" or "p":
disney_users_A_mp = {}
for index, user in enumerate(users):
    if user.startswith(('M', 'P')):
        disney_users_A_mp[user] = index

print(disney_users_A_mp)