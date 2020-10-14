'''
- List is a collection which is ordered and changeable 
- Allows duplicate members
- They are written with square brackets
'''

someList = ["Red","Green","Yellow","Orange","Blue"]
print(someList)

#Acessing items

print(someList[1])
#Outputs Green 0-based indexing


#Negative indexing 

print(someList[-1])
#Outputs Blue, negative indexing is use to access elements from last
# -1 is the index of the element


#Printing range values

print(someList[1:4])
#Outputs Green Yellow Orange prints from index till till index 3

print(someList[2:])
#Outputs from index 2 till end of the list as the end range value is not specified 


#Change element in list by accessing the specific position
someList[3] = "Purple"
print(someList)
#Outputs list with purple replaced at index 3

#Looping through
for color in someList:
    print(color)

#Checking if an item or element exists in a list

if "Red" in someList:
    print("It's there")    

#Finding the length list
print(len(someList))    

#Append or add items to list(at end)
someList.append("Orange")
print(someList)

#Insert at some specific position
someList.insert(2,"Pink")
print(someList)
#Inserts element pink at index 2 of the list(0-based indexing)
#Takes 2 argument the index position and the new element


#Remove 
someList.remove("Purple")
print(someList)
#removes Purple from list

#Pop
someList.pop()
print(someList)
#pops the last element of list

#del
del someList[1]
print(someList)
#del keyword followed by the listname with index is used to remove the element at specified position from list
#del someList deletes the entire list

#clear
someList1 = [1,2,3,4]
someList1.clear()
print(someList1)
#clear() empties the list on which it is called upon

#copy
someList1 = [1,2,3,4]
someList2 = someList1.copy()
print(someList2)
#copy is used to copy from list to another

#extend 
someList3 = [1,2,3,4]
someList4 = [5,6,7]
someList3.extend(someList4)
print(someList3)
#extend appends the list given to it at the end of the list on which it is called on

#Using the list() constructor to make a List
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


