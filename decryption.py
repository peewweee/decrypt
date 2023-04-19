# Assignment 2 PROBLEM 2 - DECRYPTION
# Phoebe Rhone L. Gangoso | BSCPE 1-4

# PSEUDOCODE
#user input string
user_input = input("Enter your text: ")
decrpt_str = ""
# check every character in string
for i in range(len(user_input)):
#   if character is "*", replace with "a"
    if user_input[i] == "*":
        decrpt_str += "a"
    else:
        decrpt_str += user_input[i]
#   if character is "&", replace with "e"
#   if character is "#", replace with "i"
#   if character is "+", replace with "o"
#   if character is "!", replace with "u"
# print encrypted string
# print output decrypted string
print(decrpt_str)