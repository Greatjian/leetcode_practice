# 201. Bitwise AND of Numbers Range

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.

## Method:

    class Solution(object):
        def rangeBitwiseAnd(self, m, n):
            """
            :type m: int
            :type n: int
            :rtype: int
            """
            count=0
            while m!=n:
                m>>=1
                n>>=1
                count+=1
            return m<<count
            
similar:

    class Solution(object):
        def rangeBitwiseAnd(self, m, n):
            """
            :type m: int
            :type n: int
            :rtype: int
            """
            while n>m:
                n&=n-1
            return n