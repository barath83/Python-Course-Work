'''
- Set is a collection which is unordered and unindexed
- Sets are written with curly brackets
- since they are unordered we may never know the order in which the items are returned
'''

thisSet = {"Jesse","Mike","Walter","Hank"}
print(thisSet)

#Accessing items 
#Only way to access is to use loops as indexing is not possible in sets

for i in thisSet:
    print(i)

#check if item exists in set

print("Mike" in thisSet)
#returns true if "Mike" is present in set here True

#Change items in a set
'''
Once a set is created we cannot change items in the set
Only new items can be added to set
'''


#Add items to set
thisSet.add("Tuco")
print(thisSet)

#Add multiple items to set
thisSet.update(["Gus","Saul"])
print(thisSet)
#update is called on the the set to add a set of items into the set which is enclosed in square brackets


#Length of set
print(len(thisSet))

#Remove item in set
thisSet.remove("Tuco")
print(thisSet)
thisSet.discard("Gus")
print(thisSet)
'''
using discard will not raise an error even if the item mentioned is not present
using remove will raise an error
'''

#pop in sets
'''
 sets are unordered pop removes the last element
 but there is no order in defining the last element 
'''

#clear in sets

thisSet.clear()
print(thisSet)
#clear empties the set
thisSet.add("Skyler")
print(thisSet)
#del keyword 
del thisSet
print(thisSet)
#this will raise a error 
# del deletes the set completely and there is no thisSet to print it out





