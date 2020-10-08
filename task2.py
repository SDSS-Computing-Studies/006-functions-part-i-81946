#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""



def largest(lists):
    lists.sort()
    answer = lists[-1]
    return answer


lists = [3,1,4,7,13,9]
print( largest(lists) )
