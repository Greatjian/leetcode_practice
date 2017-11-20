# 202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

    Example: 19 is a happy number
    
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1
    
## Method:

    class Solution(object):
        def isHappy(self, n):
            """
            :type n: int
            :rtype: bool
            """
            s=set()
            sum=0
            while n not in s:
                s.add(n)
                while n>0:
                    sum+=(n%10)**2
                    n/=10
                if sum==1:
                    return True
                n=sum
                sum=0
            return False