a ="hello"+" "+"world"
print(a)

a= "r"*10
print(a)


user=input("enter the string")
length=len(user)
print(length)


user=input("enter your name")
age= input("enter age")
print(user +" "+"is"+" "+ age + "year of old")



user="ravi"
first_letter=user[0]   #
print(first_letter)


mess="hai ravi"
part=mess[3:7]  #index 3 to 7 will prinint
print(part)


print(type(6363))   # to find data type


print(2<5)
print(3>3)

print("ABC"=="abc")
print("ABC"=="ABC")

if (True):
    print("yes")
else:
    print("no")

print("win"=="winn")

india= input("huh")
if india=="h":
    print("trofy is our")
else:
    print("no trofy")


a=int(input("enter a number:"))
if(a%5==0 and a%3==0):
    print("divisible by 3 and 5")
else:
    print("not divisible by 3 and 5")


score=int(input("enter: "))
if(score<=35):
    print("poor student")
elif(score>35 and score<70):
       print("avg student")
elif(score>70 and score<100):
     print("good student")


for i in range(100):
    print("hello")

i=10
while i <=10:
    print("helllo")

a=int(input("enter"))
counter=0
while counter<3:
    a=a+1
    print(a)
    counter=counter+1


word="python"
for each_char in word:
    print(each_char)

for i in range(10):
    print(i+(i+1))

for i in range(1,11):
    print(i,"x2=",i*2)


m=int(input("first number"))
n=int(input("second number"))
sum=0
for i in range(m,n+1):
    if(i%2==1):
        sum=sum+i
print(sum)


a=[1,2,3,4,5,6,7]
for i in a:
    print(i)


a=[1,2,3,4,5,6]
for num in a:
    if num%2==0:
        print(num,end=" ")  # wnd is use for keeping space b/w each word...

number=input("enter number: ")
print(number)
b=number.split(",")
print(b)

for i in b:
    b.index[i]=int(b.index[i])
print(b)