#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math
lists= []

x= input("Enter x:")
y= input("Enter y:")
x= float(x)
y= float(y)

def distance(x,y):
    x=x+1
    y=y+1

    lists.append(x)
    lists.append(y)

    return lists







# inputs: 
# x: any number
# y: any number
# returns: a list of 2 numbers
# function adds one to each of the input parameters and returns them
#return [ x+1, y+1 ]
print( distance(x,y) )