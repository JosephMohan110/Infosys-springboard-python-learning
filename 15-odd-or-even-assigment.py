# to check the number is odor even


print("ENTER A NUMBER TO CHECK WETHER IT IS ODD OR EVEN")
number=int(input("enter a number: "))
if number%2==0:
    print(' " ' +str( number), ' " ' + "is even")
    print(type(number))
else:
    print(' " ' +str( number), ' " ' + "is odd ")
