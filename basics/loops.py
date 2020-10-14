#if elif else snippet

a = 0
b = 50

if(b>a):
    print("b is greater than a")
elif(a>b):
    print("a is greater than b")    
else:
    print("a equals b")

#usage of and or in python

if a and b:
    print("True")
else:
    print("False")    

if a or b:
    print("True")

#the pass statement 
''' if cannot be empty but have a situation where we have a if without a content in it 
we can add a pass statement to avoid getting an error'''

if b>a:
    pass

#while loop snippet

i = 1
while i<=6:
    print(i)
    i+=1

#for loop snippet
#Looping through string

st = "Python"

for x in st:
    print(x)

for i in range(6):
    print(i)

#range(6) includes values from 0 to 5 it excludes the the value for end index and goes till before 

for j in range(2,20,3):
    print(j)

#range(2,20) starts from 2 and goes till 19 and prints value incremented by 3 for each iteration
# for loop body cannot be empty but if it is pass statement can be used 




