# 231. Power of Two

Given an integer, write a function to determine if it is a power of two.

## Method:

recursion:

    class Solution(object):
        def isPowerOfTwo(self, n):
            """
            :type n: int
            :rtype: bool
            """
            if n==1:
                return True
            if n%2 or n<=0:
                return False
            return self.isPowerOfTwo(n/2)
            
iteration:

    class Solution(object):
        def isPowerOfTwo(self, n):
            """
            :type n: int
            :rtype: bool
            """
            while n>0:
                if n==1:
                    return True
                if n%2:
                    return False
                n/=2
            return False
            
## Solution:

bit manipulation:

    class Solution(object):
        def isPowerOfTwo(self, n):
            """
            :type n: int
            :rtype: bool
            """
            if n<=0:
                return False
            return n & (n-1)==0