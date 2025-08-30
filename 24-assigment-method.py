# 1. given a string, write program to print only alphabets in the given string

# Input from user
text = input("Enter a string: ")

# Loop through each character and print only alphabets
result = ""
for ch in text:
    if ch.isalpha():      # checks if the character is a letter
        result += ch      # character will add to result

print("Alphabets only:", result)


#************************

# 2: Given a string, print all the uppercase letters in the string

text = input("Enter a string: ")

# Variable to store uppercase letters
uppercase_letters = ""

# Loop through each character
for ch in text:
    if ch.isupper():     # check if the character is uppercase
        uppercase_letters += ch

# Print the result
print("Uppercase letters:", uppercase_letters)


#*******************
