#         #    ASCII---- ORD,CHAR


# The ord() function is a built-in Python function that returns the Unicode code point of a given character.
# It essentially converts a single character into its corresponding integer representation in the Unicode standard.
# ord() only works with single characters
# ASCII: Older standard (0-127), English characters only
# Unicode: Modern standard (0-1,114,111), supports all languages and symbols
# Python's ord() uses Unicode, but ASCII values are the same in Unicode

# Input: Single character (string of length 1)
# Output: Integer representing Unicode value
# Inverse: chr() function converts back to character

# ord() and chr() are complementary functions that convert between characters and their Unicode code points


# ord() Function
# Converts character → number (Unicode code point)
# Input: Single character (string of length 1)
# Output: Integer representing Unicode value

# chr() Function

# Converts number → character (Unicode code point)
# Input: Integer (0 to 1,114,111)
# Output: Character string


# ----> ORD()

value=ord("A")
print(value)


# Uppercase letters
print(ord('A'))  # 65
print(ord('B'))  # 66

# Lowercase letters
print(ord('a'))  # 97
print(ord('b'))  # 98

# Digits
print(ord('0'))  # 48
print(ord('1'))  # 49

# Special characters
print(ord(' '))   # 32 (space)
print(ord('!'))   # 33
print(ord('#'))   # 35
print(ord('%'))   # 37


#----->  CHR()

char=chr(75)
print(char)


# Uppercase letters (A-Z)
print(chr(65))   # 'A'
print(chr(90))   # 'Z'

# Lowercase letters (a-z)
print(chr(97))   # 'a'
print(chr(122))  # 'z'

# Digits (0-9)
print(chr(48))   # '0'
print(chr(49))   # '1'

# Special characters
print(chr(32))   # ' ' (space)
print(chr(35))   # '#'
print(chr(36))   # '$'



#*********

for value in range(65,91):
    print(chr(value))

print("A"<"B")     #it compares their Unicode code points 