  #   IF

# if lets your program make decisions
# It checks a condition (True/False)
# If the condition is True  run the indented code.
# If False skip it (or run elif/else parts, if present).


a=5
if(a<5):
    print("a is small")
print("hello")   # it is taken as new block because no indentation

# student mark
score=int(input("enter your mark: "))
if (score<35):
   print("poor student")
if score > 35 and score<70 :
   print("Avg student")
if (score>70 and score<100):
   print("good student")

#******************


      #  IF - ELSE

# if checks the first condition
# elif (else-if) checks the next condition only if previous ones were False
# else runs when none of the if/elif blocks were True

india=input()
if (india=="win"):
   print("trophy is ours")
else:
   print("No trophy")


#     a number is divisible by 5 and 3

print("entere a number to check wether it is divisible by 5 and 3")
a= int(input("enter a number: "))
if(a%5==0 and a%3==0):
    print("divisible by 3 and 5")
else:
   print("not divisible by 3 and 5")



#   mark grade checking

score=int(input("enter your mark: "))
if (score<35):
   print("poor student")
elif score > 35 and score<70 :
   print("Avg student")
elif (score>70 and score<100):
   print("good student")



a=30
b=50
if(a<b):
 print("a is greatest number")
else:
 print("b is greatest ")



a=int(input("enter a number: "))
b=int(input("enter a number: "))
if a>b:
    print("hello")    #if "A" is big then it will print the "hello"
else:
    print("haii..")         ##if "A" is small then it will print the "hello"




#next one
print("IF YOUR CHILD IS ABOVE 7 YEAR OLD THE YOU SHOULD TAKE THE BUS TICKET")
print("please enter your child age")
age=int(input("Enter the age of child: "))
if age>8:     # bracket isnot important..
    print("YOU SHOULD TAKE THE BUS TICKET")    #THESE BOTH PRINT STATMENT IS CONSIDER AS A BLOCK OF STATMENT
    print("THANK YOU...CAME AGAIN")
else:
    print("CHILD AGE IS UNDER '8' TICKET NOT REQUIRED")
    print("THANK YOU...CAME AGAIN")




