'''
Dictionary is a collection which is unordered,unchangeable,indexed
Dictionaries are written with curly brackets 
They consist of keys and values
'''

thisDict = {
    "name" : "XXX",
    "sex" : "male",
    "age" : 21
}

print(thisDict)

#Accessing items 
#Items can be accessed by referring to it's key within square brackets

a = thisDict["name"]
print(a)
#this will output "XXX" as it is the value for key "name"

#get method
b = thisDict.get("name")
print(b)
#alternative method to get the value for a key

#Changing values

thisDict["age"] = 20
print(thisDict)
#outputs the dictionary with updated age values
#values can be changed by accessing it's key value

for i in thisDict:
    print(i)
#this returns all the keys in the dictionary

for j in thisDict:
    print(thisDict[j])
#this  returns all the values for each key in dictionary

for k in thisDict.values():
    print(k)       
#alternatives to print all values in dictionary

#To loop through both ket and value in dictionary

for x,y in thisDict.items():
    print(x,y)
#outputs key followed by value in a new line for each key in dictionary


#Check if key exists in dictionary
if "age" in thisDict:
    print("Yes it's there")

#Finding length of dictionary

print(len(thisDict))    

#Adding items 
#Items can be added by using a new key within square brackets and assigning it with a value

thisDict["nation"] = "Indian"
print(thisDict)

#Removing Items
#pop() method removes the item with specified key name
thisDict.pop("sex")
print(thisDict)

#popitem() removes the last inserted element
thisDict.popitem()
print(thisDict)

#del removes the item with specific key name
del thisDict["age"]
print(thisDict)

#del thisDict #this completely deletes the dictionary

#clear()
#empties the dictionary
thisDict.clear()
print(thisDict)

#Copy a dictionary
#.copy() copies elements from one dictionary to another
thatDict = {
    "id": 12
}
thisDict = thatDict.copy()
print(thisDict)

#Nested Dictionaries
#a dictionary also may contain several other dictionaries

android : {
    "nougat" : {
        "year":2016
    },
    "oreo":{
        "year":2017
    }
}