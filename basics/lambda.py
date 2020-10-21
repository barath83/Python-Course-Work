#Python Lambda functions

'''
A lambda function is a small anonymous function 
A lambda function take any number of arguments, but can have only one expression

lambda arguments : expression
'''

x = lambda a : a+10
print(x(5))
#passes 5 into a adds 5 to 10, then prints 15

#Multiple arguments

x = lambda a,b : a*b
print(x(5,6))
#takes two arguments 5 and 6, performs a*b and prints the value 30


#Why Lambda 
#lambda is more useful when they are used a anonymous function inside another function 

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#this program will double any number that is passed to it using lambda function inside myfunc