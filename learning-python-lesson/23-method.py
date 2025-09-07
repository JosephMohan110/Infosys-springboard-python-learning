#        method

# A method is just a function that belongs to an object (like a string, list, or dictionary)
# You call it using a dot (.) after the object
# Function: works on its own (example: len(text))
# Method: tied to an object, called with a dot (example: text.strip())


#      step,index.....

# An index is like the "address" of each element in a string or list
# Starts at 0. Negative indexes count from the end
# A step tells how many characters to skip while slicing
# Syntax: sequence[start:end:step]
# The step tells Python how many positions to jump

msg="-r-a-v-i"
print(msg[1:8:2])


#**********************************

    # .ISDIGIT

# It is a string method in Python
#  It checks if all characters in a string are digits (0–9 numbers)
#  It gives back True or False
#If the string has letters, spaces, minus sign (-), or dot (.), it will give False

is_digit="123456".isdigit()
print(is_digit)

is_digit="123456.0".isdigit()
print(is_digit)

is_digit="1,2,3,4,5,6".isdigit()
print(is_digit)

is_digit="123456aqwe".isdigit()
print(is_digit)

is_digit="123456,wee".isdigit()
print(is_digit)


#**************************************

# .STRIP()

# strip() is a string method in Python
# It removes extra spaces (or chosen characters) from the beginning and end of a string
# It does not remove characters from the middle
#Useful for cleaning user input (e.g., when users add extra spaces by mistake).

mobile= "     123456  "
mob=mobile.strip()
print(mob)

text = "   hello   "
print(text.strip())   # "hello"


text = "helloppp"      #Remove specific characters
print(text.strip("p"))   # "hello"


mobile= "     123456........  "
mob=mobile.strip(" . ")
print(mob)

#**************************************
 
    # .REPLACE

#  .replace() is a string method in Python
#It finds some text inside a string and replaces it with new text
#It creates a new string (because strings cannot be changed directly)
#.replace(old, new) → replaces all occurrences of old text with new text


s= "teh dog teh cat"
s=s.replace("teh","the")
print(s)


text = "I like apples"
print(text.replace("apples", "oranges"))


#***********************************************


#   .ISALPHA()

# .isalpha() is a string method
# It checks if all characters in a string are letters (A–Z or a–z)
# If yes  returns True, otherwise False

is_alpha="rahul".isalpha()
print(is_alpha)

print("Hello".isalpha())   # True
print("Python".isalpha())  # True

print("Python3".isalpha())   # False  (has a number)


#*************************************


#       ISLOWER

# .islower() is a string method
# It checks if all the letters in the string are lowercase (a–z)
# If yes returns True, otherwise False
#Numbers and symbols are ignored when checking
#False if string has uppercase letters or no letters at all.

is_lower="hai ragavI".islower()
print(is_lower)

print("python".islower())   # True
print("hello".islower())    # True

print("Python".islower())   # False (because of "P")
print("HELLO".islower())    # False (all uppercase)

print("python123".islower())  # True (letters are lowercase)


#*************************************


#     isupper

# .isupper() is a string method
# It checks if all the letters in the string are uppercase (A–Z)
# If yes returns True, otherwise False
# .isupper() True if all letters are uppercase
# False if there are lowercase letters or no letters at all
# Numbers and symbols don’t matter
# At least one letter must be uppercase


is_upper="hai JOSEPH3".islower()
print(is_upper)

print("PYTHON".isupper())   # True
print("HELLO".isupper())    # True

print("Python".isupper())   # False (has small letters)
print("hello".isupper())    # False (all lowercase)


#****************************************



#      .isalnum()

# .isalnum() is a string method in Python
# It checks if a string contains only letters (A–Z, a–z) and numbers (0–9)
# If yes → returns True, otherwise False
# (No spaces, no symbols allowed)
# .isalnum()  True if string has only letters and digits
# False if it has spaces, symbols, or is empty

is_alnum="JOSEPH".isalnum()
print(is_alnum)

print("Python123".isalnum())   # True
print("HELLO2025@".isalnum())   # false
print("12345".isalnum())       # True

print("Python 123".isalnum())  # False (space not allowed)
print("Hello!".isalnum())      # False (! not allowed)
print("2025-08-30".isalnum())  # False (- not allowed)


#**********************************************

#  .CAPTIAL

# It makes the first character of a string uppercase (capital letter)
# All the other characters in the string become lowercase
# .capitalize() → Capitalizes only the first letter, makes the rest lowercase
# Use when you want to format text properly (like names, titles, etc.)

cap="the planet is big".capitalize()
print(cap)

text = "hello world"
print(text.capitalize())   # "Hello world"

text = "PYTHON"
print(text.capitalize())   # "Python"

#*************************************


#    ..title()

# It converts the first letter of every word in a string to uppercase
# All other letters become lowercase
# .title() when you want a proper "title case" format (like book titles, names, headings)

cap="the planet is big".title()
print(cap)

text = "pYtHoN pRoGrAmMiNg laNgUaGe"
print(text.title())   # "Python Programming Language"


#***********************************************************

#    .swapcase()

# It changes uppercase letters → lowercase, and lowercase letters to uppercase
# Basically, it swaps the case of every letter in the string
# .swapcase() flips every letter’s case
# Useful when you want to invert text style (for fun, or text processing)

swap="Hello IS tfRDgg".swapcase()
print(swap)

text = "Hello World"
print(text.swapcase())   # "hELLO wORLD"

text = "Python3.0 VERSION!"
print(text.swapcase())   # "pYTHON3.0 version!"


#****************************************

      # .STARTSWITH()

# .startswith() is a string method
# It checks whether a string begins with a specified substring
# Returns True if it starts with the substring, False otherwise

s="http"
s=s.startswith("http")
print(s)

text = "Python Programming"
print(text.startswith("Python"))   # True
print(text.startswith("Java"))     # False

#***************************

        # COUNT()

# find the count of repated character
# count is a method, not a standalone function
# It belongs to string or list objects
# You call it using a dot (.) after the object


text="hello, world!"
count=text.count("l")
print(count)

text="I have a square key, if I lose my key"
count=text.count("l",2,10)
print(count)

a="FHGFHFHFfhfhfhhfFHFfg"
c=a.count("s")
print(c)

a="FHGFHFHFfhfhfhhfFHFfg"
print(a.count("h"))


#**********************

    #.INDEX()

# .index() is a method, not a standalone function
# It finds the position (index) of the first occurrence of a value in a string, list, or tuple
# If the value is not found, it raises an error (ValueError)

text="coo coo"
count=text.index("co",3,6)
print(count)

text = "hello world"
print(text.index("o"))   # 4 (first 'o' appears at index 4)


#******************************

       # .RINDEX()

# .rindex() is a string (or list) method
# It finds the last occurrence of a value in a string or list
# Returns the index position of that value
# If the value is not found, it raises a ValueError

text="I have a spare key, if I lose my key"
count= text.rindex("key")
print(count)

text = "hello world"
print(text.rindex("o"))   # 7 (last 'o' is at index 7)

#*******************************

      # .RFIND()

# .rfind() is a string method
# It finds the last occurrence of a substring in a string
# Returns the index of that last occurrence
# If the substring is not found, it returns -1 instead of raising an error (unlike .rindex())

text="I have a spare key, if I lose my key"
count= text.rfind("kEYU")
print(count)

text = "hello world"
print(text.rfind("x"))   # -1 (not found)
