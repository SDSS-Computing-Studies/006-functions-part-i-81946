#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""



def hypotenuse(a,b,c):
    import math
    if c == True:
        answer= a**2+b**2
        answer= math.sqrt(answer)
        return answer
    if c == False:
        if a>b:
            answer= a**2-b**2
            answer= math.sqrt(answer)
            return answer
        if a<b:
            answer= b**2-a**2
            answer= math.sqrt(answer)
            return answer


print("The hypotenuse is " + str(hypotenuse(3,4,True)) )
print("The hypotenuse is " + str(hypotenuse(13,5,False)) )