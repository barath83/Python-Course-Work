'''
Tuple is a collection which is ordered and unchangeable
tuples are written in rounded brackets
'''

someTuple = ("Cricket","Football","Volleyball","Basketball")
print(someTuple)

#Accessing items in tuple 
print(someTuple[0])
#returns the item at first position

#NEGATIVE INDEXING
print(someTuple[-1])
#returns the item at last position

#Indexing using ranges
print(someTuple[2:4])
#specifying ranges within the index

#Negative index ranges
print(someTuple[-3:])

#Changing tuple values 
'''
Tuples are unchangeable, or immutable
Only way is to convert the tuple to a list and change the value we want change 
and convert list back into a tuple
'''

thisList = list(someTuple)
thisList[1] = "Soccer"
someTuple = tuple(thisList)

print(someTuple)

#Looping

for i in someTuple:
    print(i)

#Check if element exists 
if "Cricket" in someTuple:
    print("Yes it's there")

#Length
print(len(someTuple))        

#Adding items to tuple 
#We cannot add items to tuple once they are created, tuples are unchangeable

#Removing item 
#Tuples are unchangeable so one item cannot be removed but we can delete the tuple completely

del someTuple
print(someTuple) #this will raise an error as tuple is deleted already

