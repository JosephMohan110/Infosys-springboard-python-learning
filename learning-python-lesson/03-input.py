  #INPUT FUNCTION....

#input() is used in Python to ask the user to type something
# Whatever the user types will be stored in a variable
# By default, it is saved as text (string)


input()   # in bracket we can enter anyting...we can enter prompt...

user=input("enter a string: ")
length=len(user)
print(length)


user=input("enter your name: ")
age=input("enter your age: ")
print(user+ "is" + age +"year of old")

user="joseph"
first=user[4]
print(first)

#input(jose)     # it cause error....


input("Enter your age:\n")      #what all thing we written in te input that all consider as a string...if it is number or charater tese all consider as a string..
                                #after age we put /n so age will print downward..


print("Nice place"+" "+input("where is your place:"))    #function nu inside ill ulla function first process cheyum..here inside input so first input will process..
                                                            #input anne word nu comma kodukanda...


print("Hey"+" "+input("what is your name:")+" how are you ?")     #using concatention of string we can print input string and print 

                 #OR
                 
print("Hey"+" "+input("what is your name:")+" "+"how are you ?")




