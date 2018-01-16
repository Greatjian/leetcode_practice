# 441. Arranging Coins

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

    n = 5
    
    The coins can form the following rows:
    ¤
    ¤ ¤
    ¤ ¤
    
    Because the 3rd row is incomplete, we return 2.

Example 2:

    n = 8
    
    The coins can form the following rows:
    ¤
    ¤ ¤
    ¤ ¤ ¤
    ¤ ¤
    
    Because the 4th row is incomplete, we return 3.
    
## Method:

direct method, too slow:

    class Solution(object):
        def arrangeCoins(self, n):
            """
            :type n: int
            :rtype: int
            """
            i=1
            while n>=i:
                n-=i
                i+=1
            return i-1
            
## Solution:

using math, sum = (x + 1) * x / 2 <= n

x = (Math.sqrt(8 * n + 1) - 1)/ 2

    class Solution(object):
        def arrangeCoins(self, n):
            """
            :type n: int
            :rtype: int
            """
            return int(((8.0 * n + 1)**0.5 - 1) / 2)