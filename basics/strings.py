#Strings in python are string literals surrounded by either double or single quotes

a = "Hello Py"
print(a)

#Multiline strings 
#They are enclosed within three single quotes pr three double quotes
b = '''Hi welcome to 
python's multiline
string!
'''
print(b)

#Strings in python are arrays of bytes representing unicode characters
# There are no char in python therefore each letter in a string is of length 1 and it is a string
#Prints the third letter in this example
#Prints 'h' as per 0 based indexing
c = "Python"
print(c[3])


#Slicing
#Can return a range of characters within the string by specifying a start and end index

d = "Problem solving"
print(d[2:9])

#Outputs oblem s based on 0-indexing 
#9th index is not included which means that starting index is included 
#ending index is excluded 


#Negative Indexing
#to start slicing from the end of the string

e = "Problem solving"
print(e[-5:-1])

#Outputs lvin as it starts from the last character g and goes backwards
#since g is -1 and end index is not considered it slicing so it stops till n

#String length can be found using length method

print(len(e))

#Lower to Upper and vice versa
f = "Hello World Python"
print(f.lower())
print(f.upper())

#Replace a word with another word
print(f.replace("H","J"))

#Checking for a specific string in a given string
#returns a boolean 
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)


#String formatting

age = 21
txt = "My name is Barath and I'm {} years old"
print(txt.format(age))



