'''
A function is a block of code which only runs when it is called.
You can pass data,known as parameters,into a function.
It returns a result
'''

#python function is defined using the def keyword
#samplefunc is the user defined function name
def samplefunc():
    print("Python function works!")

samplefunc()    


#Arguments
'''
Data can be passed into functions as arguments.
Arguments are specified after function name within the paranthesis,we can add many number of arguments seperated by commas.
'''

def sayHello(name,age):
    print("Hello "+name+","+age+" Welcome to python function")

sayHello("Barath","21")    


#Parameter Vs Arguments
'''
Parameter and argument are used for the same thing,information passed to function
From function's perspective
- A parameter is the variable listed inside the parantheses in the function defintion
- An argument is the value that is sent to the function when it is called.
'''

#Arbitrary arguments 

'''
If we don't the specific number of arguments that will be passed to our function, add a * before the parameter name in function definition
So that the function receives a tuple of arguments and can access items accordingly
'''

def functionargs(*suits):
    print("The Coolest Suits Character is "+suits[2])

functionargs("Mike","Harvey","Donna");    

    