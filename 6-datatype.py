
            

       #TO FIND THE DATA TYPE:::: int,float,string,bollan,list,range,tuple,complex are data type...

# INT: no range EX: 64673783893937464....INT can be binary poctal hexadecimal type can form



name= 3
print (type(name))    # we can find what type of value is entered in variable by useing "TYPE"

              # we should not requried define dta type.EX; in C we type int var=3; in python int is not requried

name="joseph"        #to find data type of string
print(type(name))



varible_1=1     #Here varible_1 and varible_2 will add togther, after adding answer is float then print float, if it is integer then print int 
varible_2=20.88            #varibles total sum will take and its datatype will sow
print(type((varible_1)+(varible_2)))


varible_1=1     #Here varible_1 and varible_2 will add togther and answer will show
varible_2=20.88
print((varible_1)+(varible_2))    



varible_1=1     #Here varible_1 and varible_2 will add togther and answer and data type will show will show
varible_2=27.88
print((varible_1)+(varible_2))    
print(type((varible_1)+(varible_2)))



              #FLOAT NUMBER.....

     #FLOAT : 3.3333,3,33.2221


print(type(335.7e3))
a= int (input("enter 1 number"))
l= int (input("enter 2 number"))
print(a+l)





#COMPLEX NUMBER

#complex number means real number + imaginary number.

s=3+4j
print(type(s))
print(s)





#BOLLEAN

#A Boolean is a data type that has only two possible values: ture and false

a= 5>7    #5 and 7 will compare, then statment is ture it will ture bse on bollen data type
print(a)
print(type(a))     #data type is boolen

a= 5>2     # here statment is ture oso output is ture
print(a)



#STRING

#A string in Python is just text inside quotes.

print("hello")

aa= ("hello"+ "world")
print(aa)
print(type(aa))


print("hello" * 100)   # *100 means the word hello will pirnt 100 times




#  LIST...

# A list in Python is like a collection of items kept inside square brackets [ ]
# Items can be numbers, text, or even mixed
# You can change (add, remove, update) items in a list → lists are mutable

mylist=[1,2,3,4,5,6]
print(mylist)
print(type(mylist))


my_list=[3,5,3.4,7.3,0.2,"english",True]
print(my_list)
print(type(my_list))


lists=[3,5,3.4,7.3,0.2,"english",True]
lists.append(3)   #add a item into the list using 
lists.append(9)
print(lists)
print(type(lists))
print(lists[6])
print(lists[1:6])     #oru particular element na print cheyan
print(len(lists))     # to find the length of list ,to find the the number of element 



      #empty list

li=[]   #empty list
print(li)
li.append(10)    #add element to list
print(li)


   #delete a element

list1=[3,5,3.4,7.3,0.2,"english",True]
print(list1)
del list1[3]  #index 3 is deleted
print(list1)


  #join 2 list

list1=[1,2,3,4]
list2=[5,6,7,8]
list3=list1+list2
print(list3)



     # TUPLE DATA TYPE

# A tuple in Python is just like a list, but with one big difference → you cannot change it (it is immutable).
# Written inside round brackets ( )
# Can store numbers, text, or mixed items
# You cannot add, remove, or change values once created

tuple1=(1,2,3,4)
print(tuple1)
print(type(tuple1))
print(len(tuple1))    #length of tuble can be find

#multiple data type is allowed
tuple2=(1,2,3,3.44,'english', True,3)
print(tuple2)

# converte list into tuple
list1=[1,2,"hello",True]
print(list1)
changed=tuple(list1)   # list is converted ito tuple and store into the varible"changed"
print(changed)


#converted tuple into list

tuple1=(1,2,3,3.4)
print(tuple1)
changed=list(tuple1)   #tuple is changed into list 
print(changed)



     #SET

# A set in Python is a collection of unique items written inside curly braces { }
# No duplicate values allowed
# Order is not fixed (items may appear in any order)
# Useful for things like removing duplicates or doing math operations (union, intersection, etc.)
    
set1={1,2,3,4}
print(set1)
print(type(set1))
print(len(set1))


#convert list into set
list=[4,5,6,False]
print(list)
change3=set(list)  #list change into set
print(change3)

#repated value automaticallly deletd
set2={1,2,23,3,3,3,}
print(set2)



       