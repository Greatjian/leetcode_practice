# 069. Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.

Example 1:

    Input: 4
    Output: 2

Example 2:

    Input: 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.
    
## Method:

cheating...

    class Solution(object):
        def mySqrt(self, x):
            """
            :type x: int
            :rtype: int
            """
            return int(x**0.5)
            
## Solution:

binary search:

    class Solution(object):
        def mySqrt(self, x):
            """
            :type x: int
            :rtype: int
            """
            left, right=0, x
            while left<=right:
                mid=(left+right)/2
                s=mid*mid
                if s==x:
                    return mid
                elif s<x:
                    left=mid+1
                else:
                    right=mid-1
            return right
            
Newton's iterative method:

    class Solution(object):
        def mySqrt(self, x):
            """
            :type x: int
            :rtype: int
            """
            n=x
            while x*x>n:
                x=(x+n/x)/2
            return x