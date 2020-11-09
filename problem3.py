#! python3
"""
Create a function called factors()
Input parameter is a positive integer
Output is a sorted list containing all of the factors of that number.
Note: A Factor is a positive integer that can be evenly divided
into another number.
Example: The factors of 10 are 1, 2, 5, 10
(2 points)
"""
x= input("Enter a positive integer:")
x= int(x)
lists= []

def factors(x):
    for i in range(1,x+1):
        if x%i==0:
            lists.append(i)
    
    return lists

print( factors(x) )

           

