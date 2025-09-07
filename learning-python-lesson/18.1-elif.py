 # ELIF

# elif stands for “else if”.
# It is used in conditional statements when you have multiple conditions to check.
# Python checks the conditions from top to bottom:
# if  first condition
# elif  additional conditions
# else  runs if none of the above conditions are true

# MARK..

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")


#HEIGHT
print("hai please enter your age and height")
age=int(input("ENTER YOUR AGE: "))
height=int(input("ENTER YOUR HEIHT(in feet):' "))
if height>=3:   # it is main "if for heght"
    if age<=10:  #this is statment for age...different age checking
        print("ticket amount is '100'")
    elif age<=50:
        print("TICKET PRICE IS '500'")
    else:     #if age is not below 10 and above 50 the it will execute..    age ent else
        print("TICKET AMOUNT IS '300'")
else:       #height enet else
    print("you are not eligable, beacuse your height is below eligable critiea")
