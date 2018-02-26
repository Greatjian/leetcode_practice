# 790. Domino and Tromino Tiling

We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These shapes may be rotated.

    XX  <- domino
    
    XX  <- "L" tromino
    X

Given N, how many ways are there to tile a 2 x N board? Return your answer modulo 10^9 + 7.

(In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.)

Example:

    Input: 3
    Output: 5

Explanation: 

    The five different ways are listed below, different letters indicates different tiles:
    XYZ XXZ XYY XXY XYY
    XYZ YYZ XZZ XYY XXY

Note:

- N  will be in range [1, 1000].

## Method:

in contest, O(n^2):

    class Solution(object):
        def numTilings(self, N):
            """
            :type N: int
            :rtype: int
            """
            if N==0:
                return 0
            if N==1:
                return 1
            if N==2:
                return 2
            dp=[0]*(N+1)
            dp[0], dp[1], dp[2], dp[3]=1,1,2,5
            for i in range(4, len(dp)):
                for j in range(i-1, -1, -1):
                    if j==i-1 or j==i-2:
                        dp[i]+=dp[j]
                    else:
                        dp[i]+=2*dp[j]
                dp[i]%=10**9+7
            return dp[N]
            
actually, same idea can be achieved in O(n) time:

    class Solution(object):
        def numTilings(self, N):
            """
            :type N: int
            :rtype: int
            """
            dp=[1]*(N+1)
            s=2
            for i in range(2, len(dp)):
                dp[i]=(2*s-dp[i-1]-dp[i-2])%(10**9+7)
                s+=dp[i]
            return dp[-1]