# 633. Sum of Square Numbers

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

    Example 1:
    
    Input: 5
    Output: True
    
    Explanation: 1 * 1 + 2 * 2 = 5
    
    Example 2:
    
    Input: 3
    Output: False
    
## Method:

square number: (int(a**0.5))**2==a

    class Solution(object):
        def judgeSquareSum(self, c):
            """
            :type c: int
            :rtype: bool
            """
            for i in range(int(c**0.5+1)):
                res=int((c-i**2)**0.5)
                if res**2==c-i**2:
                    return True
            return False
            
## Solution:

two pointers:

    class Solution(object):
        def judgeSquareSum(self, c):
            """
            :type c: int
            :rtype: bool
            """
            l, r=0, int(c**0.5)
            while l<=r:
                if l**2+r**2==c:
                    return True
                elif l**2+r**2<c:
                    l+=1
                else:
                    r-=1
            return False