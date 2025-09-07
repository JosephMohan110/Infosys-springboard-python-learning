#           for loop

#A for loop is used to repeat a block of code for each item in a sequence (like a list, string, or range of numbers).
# A for loop is used to repeat code
# It goes through each element of a sequence (list, string, tuple, dictionary, or range)
# Useful for iteration (repeating tasks)



for i in range(1,6):
    for j in range(1,3):
        print(j,"apple")


for i in range(1,3):
    print("week:",i)
    for j in range(1,4):
        print("day:",j)


for i in range(1,5):
    print()    # blank will be print
    for j in range(1,i+1):
        print(j,end="")

#multiplaction table of 2
for i in range(1,11):
    print("2x",i,"=",2*i)


#     BREAK

# The break statement is used to stop a loop immediately
# When Python sees break, it jumps out of the loop (even if items are left)
# break Stops the loop early
# Useful when you don’t need to continue once a condition is met (like finding something)

for i in range(5):
    if i==3:
        break
    print(i)
print("end")



#     CONTINUE IN FOR LOOP

#The continue statement is used to skip the current loop step and move to the next one
#Unlike break, it does not stop the loop completely

for i in range(10):
    if i==3:
        continue
    print(i)
print("end")


# skip even numbers
for num in range(1, 6):
    if num % 2 == 0:
        continue   # skip even numbers
    print(num)



#       PASS

# pass means “do nothing”
# It is used when Python expects a statement but you don’t want to write any code yet
# The loop (or function/class) will just skip that part and continue normally

for i in range(10):
    pass
