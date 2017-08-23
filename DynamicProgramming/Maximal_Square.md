# 221. Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:
    
    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0

Return 4.

## Method:
dp，注意状态转移方程：dp[i][j]=min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1

建立二维数组：dp=[[0]*n for i in range(m)]

    class Solution(object):
        def maximalSquare(self, matrix):
            """
            :type matrix: List[List[str]]
            :rtype: int
            """
            if not matrix:
                return 0
            m,n=len(matrix),len(matrix[0])
            dp=[[0]*n for i in range(m)]
            ans=0
            for i in range(m):
                for j in range(n):
                    dp[i][j]=int(matrix[i][j])
                    if i and j and dp[i][j]:
                        dp[i][j]=min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
                    ans=max(ans,dp[i][j])
            return ans*ans