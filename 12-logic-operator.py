
# 3 LOGICAL OPERATERS (and, or, not). it is used to combain two statment conditions...
# 3 OPERATION SHOULD BE WRITE IN SMALL LETTER..


#  *** AND OPERATION***


#   it work based on...... 1 means ture... and 0 means false...
#   1      1    = 1(ture)
#   1      0    = 0(false)
#   0      1    = 0(false)
#   1      1    = 1(ture)


a,b=3,4     # a=3, b=4.....
print(a<5 and b<3)   # HERE AND IS OPERATERS... if any of condition became worng then it became false...both condition should be correct then only it became ture...
print(a<5 and b>3)    #in c program we use & symbol
#print(A<5 and B==4)  # variable should be write in small letter as declered as. if it declare as small letter then it should be write in small letter
print(a>2 and b==4)   # here 2 condition is ture(a>2 and b==4) so, out is ture.. 2 condition will do and operation then out will ture...





#  ***OR OPERATON****

#ANY ONE CONDITION ONLY TO BE TURE THEN OUT PUT WILL BE TURE....1 MEANS TURE... AND 0 MEANS FALSE....

#     1       1   = 1
#     1       0   = 1
#     0       1   = 1
#     0       0   = 0


A,B =5,9
print(A<4 or B>10)   # A is false B is false and output is false
print(A<10 or B>10)   #A  is ture and B is false out is ture
print(A<6 or B>8)   # A is ture B is ture out is ture
print(A<=5 or B>=9)
print(A<=5 or B<=9)




#  ***NOT OPERATER***

#IT WILL REVERSE THE RESULT


#     1       = 0
#     0      =  1


a=True 
print(not(a))   # inprint function if we write "c" instread of "a" then it case name error...


a=5
print(not(a))  #A is 5 it is correct and its opposite is false..false will print as output..



a=3
b=6
c=True
print(a<=3 ,not(c))
print(a<=3 and not(c))   # here first a<=3 condition will take then not(c) condition will take and both result will done AND operation...then output willl get...
print(a<=3 or not(c))   #any one condition only ned to be ture ...bcause or operaoris use




