#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""
a= input("What is a")
a= float(a)

def isInteger(a):

    answer=a.is_integer()



    return answer

print( isInteger(a) )