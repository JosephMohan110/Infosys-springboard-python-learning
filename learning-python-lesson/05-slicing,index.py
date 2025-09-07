      # SLICING
#IF I WANT TO PRINT A SMALL POSITON PF STRING WE USE SLICING... IT DONE BY USING ARRAY

           # Indexing
# Every character in a string has a position number (index)
# Starts from 0 for the first character
# Negative index means counting from the end

word = "Python"
print(word[0])   # P  (first letter)
print(word[2])   # t  (3rd letter)
print(word[-1])  # n  (last letter)

user="joseph"
first=user[4]
print(first)


        # Slicing
# Slicing means cutting a part of the string

word = "Python"
print(word[0:4])   # Pyth  (from 0 to 3)
print(word[2:6])   # thon (from 2 to 5)

ab= ("hello how are you")
print(ab[0:7])
print(ab[1:10])
print(ab[5:10])  # each character are index from 0 to...... 0 = h, 1 = e, 
print(ab[2:10])   #space also counted in the array
print(ab[8:7])    # nothing will print it should be in order


     #STEP
# Step in slicing
# We can also tell Python to jump characters using a step

word = "Python"
print(word[0:6:2])   # Pto  (takes every 2nd letter)
print(word[::-1])    # nohtyP  (reverses string)


nm=("HAII YOU ARE MILLINOR")
print(nm)
print(nm[0:9:2])  # there 3 values is there 2 means every 2nd letter will remove or multiple of 2 index corresponding letter will remove
print(nm[0:14:1])