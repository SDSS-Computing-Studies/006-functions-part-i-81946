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
lists2= []

x= input("Enter x:")
y= input("Enter y:")
x= float(x)
y= float(y)
lists.append(x)
lists.append(y)

a= input("Enter x2:")
b= input("Enter y2:")
a= float(a)
b= float(b)
lists2.append(a)
lists2.append(b)
def distance(lists,lists2):
    d1= lists[0]+lists[1]
    d2= lists2[0]+lists2[1]
    

    d= d2-d1

    return d







# inputs: 
# x: any number
# y: any number
# returns: a list of 2 numbers
# function adds one to each of the input parameters and returns them
#return [ x+1, y+1 ]
print( distance(lists,lists2) )