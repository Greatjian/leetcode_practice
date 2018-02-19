# 279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

## Method:

dp, tle:

    class Solution(object):
        def numSquares(self, n):
            """
            :type n: int
            :rtype: int
            """
            dp=[float('inf')]*(n+1)
            dp[0]=0
            for i in range(1, n+1):
                if (int(i**0.5))**2==i:
                    dp[i]=1
                    continue
                for j in range(i+1):
                    dp[i]=min(dp[i], dp[j]+dp[i-j])
            return dp[-1]
            
## Solution:

no need to check every j, still tle:

    class Solution(object):
        def numSquares(self, n):
            """
            :type n: int
            :rtype: int
            """
            dp=[float('inf')]*(n+1)
            dp[0]=0
            for i in range(1, n+1):
                j=1
                while j*j<=n:
                    dp[i]=min(dp[i], dp[i-j*j]+1)
                    j+=1
            return dp[-1]