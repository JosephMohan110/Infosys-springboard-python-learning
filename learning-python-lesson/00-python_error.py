print(len("jose"))   
#print(len(jose)) #if we don't put inverted comma FOR jose an error occur..print(len("jose"))    "NAME ERROR"
                  #only string value length can be find..but, value jose is not in inverted comma...so it cant find...



print(len("1234567"))
#print(len(1234567))  #if we don't put inverted comma FOR 1234567 an error occur..print(len("1234567"))
                      #only string value length can be find..it is integer value so ...."TYPE ERROR".... if we put inverted comma to integer value then integer value will converted into string and length can find..
                      #here integer value is given, but it will converted into string using doubble inverted comma...


#OUT SHOULD BE 5 CARATER IN YOUR INPUT.... 

print("ENTER SOMETHING THAT YOU LIKE & FIND ITS LENGTH..")  #a error will occur if we type like "PRINT"'
A=input("ENTER HERE:")                                      #What all things we write here that all will store into the variable "A"
length=len(A)                                               #value stored in variable "A" ,will calculated here...and it store into varible "length"....
print("There are "+str(length)+" charater")       #In print, only string can concatenate..integer(INT) not possible..so, we want to convert length(it is int) into string for tis we use "str"
#print("There are "+(length)+" charater")  #if we dont put str error will occur...TypeError: can only concatenate str (not "int") to str...
          #not required..
#F=str(length)    #small letter f also can be use..this step and below 2 step is same...as before line length is converted and not stored...here it is stored in "f" variable...
#print(type(F))
A=str(length)             #str(length) value is stored into the variable "A"
print(type(str(length)))    #str(length).. here integer is converted into string.. using this line of code we can check it is coverted or  if it is converted it show "class str"
print(type(length))      #ere data type of length can see..




#A="jose"
#print(10 +(A))    #It will type error,jose is stored in "A" variable..and it is string..we want to convert into integer for adding with 10

#A="jose"
#print(10 +int(A))   # value error...value stored in variable "A" is not integer.. if replace "jose" into 123 te code will run

A="12324"
print(10 +int(A))     # it will work 10 will add wit with variable "A"






      #DIFFERENT TYPE OF ERRORS....

#syntax error= WORNG FORMAT..in assigment operation format is a=2,but 2=a or 5=5 this willl syntax error..because, in LHS integer should not possibl only variable()
#name error=
#type error=
#value error=    we cant convert name(string value) into integer...
               # name="joseph"       ***NOT POSSIBILE..ERROR***
               # print(int(name)).....
               # we can convert integer as a string..
               #name="123456"           ****possible****
               #print(int(name))
                          