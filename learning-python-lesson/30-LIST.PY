# #         LIST=[]


# A list in Python is a collection of items (called elements).
# It can store different types of data: numbers, strings, floats, or even another list.
# A list is ordered (the order you put items stays the same).
# A list is mutable (you can change it after creation — add, remove, or update items)
# It can hold multiple items in one variable.
# Dynamic → size can grow or shrink.
# Easy to access, update, and slice data.
# Supports many built-in methods like append(), remove(), sort(), etc.


a=16
lista=[5,"True",10.11,a]
print(type(lista))
print(lista)


lista=[5,'False',8.2]
listb=[1,lista]
print(listb)

lista=[5,'False',8.2]
print(len(lista))

lista=[5,"True",9.0,"raahg"]
print(lista[2])

lista=[5,"True",9.0,"raahg"]
for item in lista:
    print(item)


lista=[1,2,3]
listb=["a","b","c"]
listc=lista+listb
print(listc)


lista=[]
print(lista)
for i in range(1,4):
    lista+=[i]
print(lista)


lista=[1,2]
listb=lista*3
print(listb)


lista=[5,"false",8.2]
listb=lista[:2]
print(listb)


lista=["d","e","t","w","a"]
listb=lista[0:5:3]
print(listb)


color="yellow"
lista=list(color)
print(lista)


lista=list(range(11))
print(lista)

lista=[1,2,3,5]
print(lista)
lista[3]=4
print(lista)