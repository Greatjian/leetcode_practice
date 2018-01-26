# 191. Number of 1 Bits

Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

    For example, 
    
    the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, 
    so the function should return 3.

## Method:

    class Solution(object):
        def hammingWeight(self, n):
            """
            :type n: int
            :rtype: int
            """
            return sum(map(int, bin(n)[2:]))
            
            // bin(n).count("1")
            
## Solution:

Without using bin(), just bits manipulaition:

    class Solution(object):
        def hammingWeight(self, n):
            """
            :type n: int
            :rtype: int
            """
            res=0
            while n:
                n=n&(n-1)
                res+=1
            return res
            
and:

    class Solution(object):
        def hammingWeight(self, n):
            """
            :type n: int
            :rtype: int
            """
            res=0
            while n:
                res+=n&1
                n>>=1
            return res