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
#   if character is "&", replace with "e"
    elif user_input[i] == "&":
        decrpt_str += "e"
#   if character is "#", replace with "i"
    elif user_input[i] == "#":
        decrpt_str += "i"
#   if character is "+", replace with "o"
    elif user_input[i] == "+":
        decrpt_str += "o"
#   if character is "!", replace with "u"
    elif user_input[i] == "!":
        decrpt_str += "u"
    else:
        decrpt_str += user_input[i]
# print encrypted string
print("Encrypted text: ", user_input)
# print output decrypted string
print("The Plain Text:")
print(decrpt_str)