# 50. Pow(x, n)

Implement pow(x, n).

Example 1:

    Input: 2.00000, 10
    Output: 1024.00000

Example 2:

    Input: 2.10000, 3
    Output: 9.26100
    
## Method:

n-=1 in each turn, tle:

    class Solution(object):
        def myPow(self, x, n):
            """
            :type x: float
            :type n: int
            :rtype: float
            """
            if n==0:
                return 1
            if n<0:
                x=1.0/x
                n=-n
            t=x
            while n-1:
                x*=t
                n-=1
            return x
            
## Solution:

n/2 in each turn:

recursion:

    class Solution(object):
        def myPow(self, x, n):
            """
            :type x: float
            :type n: int
            :rtype: float
            """
            if n==0:
                return 1
            if n<0:
                x=1.0/x
                n=-n
            if n%2:
                return x*self.myPow(x*x, n/2)
            return self.myPow(x*x, n/2)
            
iteration:

    class Solution(object):
        def myPow(self, x, n):
            """
            :type x: float
            :type n: int
            :rtype: float
            """
            if n==0:
                return 1
            if n<0:
                x=1.0/x
                n=-n
            res=1
            while n:
                if n%2:
                    res*=x
                x*=x
                n/=2
            return res
            
            