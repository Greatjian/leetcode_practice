# 172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

## Method:

iterative:

    class Solution(object):
        def trailingZeroes(self, n):
            """
            :type n: int
            :rtype: int
            """
            res=0
            while n:
                res+=n/5
                n/=5
            return res
            
recursive:

    class Solution(object):
        def trailingZeroes(self, n):
            """
            :type n: int
            :rtype: int
            """
            if not n:
                return 0
            return n/5+self.trailingZeroes(n/5)