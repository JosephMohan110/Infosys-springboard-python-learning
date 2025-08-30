                #   ASSIGMENT OPERATER

#   ASSIGMENT OPERATER..."  = "   (+,-,*,%,**)these all can came in assigment operater...
#Assignment operators are used to give a value to a variable.
# The main one is = (equal sign).
# Others combine math with assignment.


a=5       # value 5 will store  in variable "a"..now "a" means 5...
a=a+5     #it consider as "a=5" so, 5+5 =10 (just addition take place)...
print(a)    #

#    OR(shorthand operaters)
          #in above aswer again 5 will add and print the result 
a+=5      #  when we expand this we get *** a=a+2***  LHS =a ,  then equal to,after.. symbol(+) ent front ill oulla variable na azhutha after equal to(value store cheyuthakuna variable evida varum..) then write RHS (a=2)...this is short hand operaters..result willl a=a+5
#print("a")   #if we put like this only alphabet "a" will print..
print(a)


s=10
s-=10    #here s is 10, so 10 -10 =0 
print(s)

q=4          #these shorthand can done on every operaters..
q-=4
print(q)

l=4
l=l-4
print(l)


a,b,c=5,6,7 
print(a,b,c)

#SHORTHAND OPERATERS
a=6
a*=3
print(a)


A,S,D=3,7,4
print(A,S,D)
A-=D  #  A=A-D.....(A=3-4).. VALUE OF "A" IS 3 AND VALUE OF "D" IS 4 AND JUST ADDITION
print(A)



a,b=4,3
c=a+b     #7
a+=2     #6 
c+=a
c/=a     #c=c/a...c=7/2
c//=a   # to avoid float number
print(c,c)



q,w=5,7
e=q+w
w/=(2*4)   # expand...w=w/(2*4).....w=7/(8)  #in division floating number will give
e+=w
print(e)  #here first "w" value calculated then will add with "e"
print(w)