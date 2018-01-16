# 640. Solve the Equation

Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:

    Input: "x+5-3+x=6+x-2"
    Output: "x=2"

Example 2:

    Input: "x=x"
    Output: "Infinite solutions"

Example 3:

    Input: "2x=x"
    Output: "x=0"

Example 4:

    Input: "2x+3x-6x=x+2"
    Output: "x=-1"

Example 5:

    Input: "x=x+2"
    Output: "No solution"
    
## Method:

等式左右共四个常数：

    class Solution(object):
        def solveEquation(self, equation):
            """
            :type equation: str
            :rtype: str
            """
            l, r=equation.split('=')[0], equation.split('=')[1]
            l1, l2, r1, r2=0, 0, 0, 0
            for i in l.replace('+', ' +').replace('-', ' -').split():
                if i[-1]=='x':
                    if i=='+x' or i=='x':
                        l1+=1
                    elif i=='-x':
                        l1-=1
                    else:
                        l1+=int(i[:-1])
                else:
                    l2+=int(i)
            for j in r.replace('+', ' +').replace('-', ' -').split():
                if j[-1]=='x':
                    if j=='+x' or j=='x':
                        r1+=1
                    elif j=='-x':
                        r1-=1
                    else:
                        r1+=int(j[:-1])
                else:
                    r2+=int(j)
            # print l1, l2, r1, r2
            if l1==r1:
                if l2!=r2:
                    return "No solution"
                else:
                    return "Infinite solutions"
            return "x=%d" %((r2-l2)/(l1-r1))
            