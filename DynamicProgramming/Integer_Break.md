# 343. Integer Break

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.

找规律：

    2  ->  1 * 1
    3  ->  2 * 1
    4  ->  2 * 2
    5  ->  3 * 2
    6  ->  3 * 3
    7  ->  3 * 2 * 2
    8  ->  3 * 3 * 2
    9  ->  3 * 3 * 3
    10 ->  3 * 3 * 2 * 2
    11 ->  3 * 3 * 3 * 2
    12 ->  3 * 3 * 3 * 3
    13 ->  3 * 3 * 3 * 2 * 2
    
## Method:

dp递推公式：dp[i]=max(3 * dp[i-3], 2 * dp[i-2])

    class Solution(object):
        def integerBreak(self, n):
            """
            :type n: int
            :rtype: int
            """
            if n<=3:
                return n-1
            dp=[0]*(n+1)
            dp[2],dp[3]=2,3
            for i in range(4,n+1):
                dp[i]=max(3*dp[i-3],2*dp[i-2])
            return dp[-1]
            
根据除以3余数找规律：

    class Solution(object):
        def integerBreak(self, n):
            """
            :type n: int
            :rtype: int
            """
            if n == 2:
                return 1
            elif n == 3:
                return 2
            mod = n % 3
            if mod == 0:
                return 3 ** int(n / 3)
            elif mod == 1:
                return 3 ** int(n / 3 - 1) * 4
            else:
                return 3 ** int(n / 3) * 2
            