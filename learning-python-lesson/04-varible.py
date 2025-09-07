        #VARIBLES..........

#,special symbol like ?"|}{ } these are not allowed begin of variable...number also not allowed like 12344.."

# A variable is just a name you give to store some information in a program
# It’s like a small box with a label on it. You can keep something inside the box and use it later

#      not variable...


#  roll no
#"age"


#valied variable...
 
#age=
#age_1=
#id=




#name = input("wat is your name:")     #Here name is .. so,wen we enter te name or data as input it will store in varible "name". Here we can ask input value from user.
#print(name)


#name = "jose"     #Here name is already enter by the programer...so user cant enter..... input value is given by programer...
#print(name)




                      #TO FIND LENTH OF STRING

name = input("wat is your name: ")       #if we write any number in input then, input will consider as a string
length=len(name)                         #input value will store in variable (name).........
print("length of string is:")
print(length)


          #OR

print("ENTER SOMETHING THAT YOU LIKE & FIND ITS LENGTH..")  
A=input("ENTER HERE:")
length=len(A)
print("There are "+' " '+str(length)+' " '+" charater")     #if we not give str then length will not convert..in print function string value olny will take..so we want to convert length to string for that we use str....
                                               #first str function will consider then only ..then only print function will consider..