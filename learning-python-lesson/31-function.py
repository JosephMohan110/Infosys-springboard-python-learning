     #     FUNCTION.....



# def add():
#     a=int(input("enter a number: "))
#     b=int(input("enter a numer: "))
#     print(a+b)
# add()



# def sub():
#     a=int(input("enter a number: "))
#     b=int(input("enter a numer: "))
#     print(a-b)
# sub()


# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# sub(5,3)
# add(10,5)



# def printrange(r1,r2):
#     for i in range(r1,r2):
#         print(i)
# printrange(1,11)


# def painter():
#     return "i am painter"
# msg=painter()
# print(msg)



def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))



def recursive_function(n):
    if n==0:
        return
    print(n)
recursive_function(n-1)
recursive_function(3)


user = "jose"
password="123"
un=input("enter user name: ")
pw=input("enter the password: ")

def validate():
    if(user==un and password==pw):
        return True
    else:
        return False
a=validate()
print(a)