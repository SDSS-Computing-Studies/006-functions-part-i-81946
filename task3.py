#!python3
"""
Create a function called perimeter()
The input is a list.
The return value is the sum of all the numbers in the list
added together
(2 points)
"""

a= input("a")
a= float(a)
b= input("b")
b= float(b)
c= input("c")
c= float(c)
d= input("d")
d= float(d)

lists= [a, b, c, d]
def perimeter(lists):
    answer= a+b+c+d
    return answer

print( perimeter(lists) )
