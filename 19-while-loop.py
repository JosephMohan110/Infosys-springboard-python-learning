    #while loop

# A while loop is used to repeat a block of code again and again as long as a condition is True
# When the condition becomes False, the loop stops
# When you don’t know in advance how many times to repeat
# Keep asking user to enter password until it’s correct

a=int(input("enter a number:"))
counter=0
while counter<3:
    a=a+1
    print(a)
    counter=counter+1


i = 1
while i <= 5:   # condition
    print(i)    # code to run
    i = i + 1   # update


i=int(input("enter a number: "))
while(i>0):
    print(i)
    # i=i+1   #dont run it it will pirnt infinite

#****************

        # While loop with break
#The break statement is used to completely stop a loop.
#When Python sees break, it jumps out of the loop immediately, even if the loop condition is still True

i = 1
while i <= 10:
    if i == 6:
        break   # stop when i = 6
    print(i)
    i = i + 1


    # While loop with continue
#The continue statement is used to skip only the current iteration of the loop.
#It doesn’t stop the loop entirely  it just jumps to the next round of the loop.

i = 0
while i < 5:
    i = i + 1
    if i == 3:
        continue   # skip 3
    print(i)
