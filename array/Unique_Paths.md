# 062. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

## Method:
数学题，每条路是其上方与左侧可能性之和。

初始条件：最上方与最左侧可能性为1。

代码实现：

    class Solution(object):
        def uniquePaths(self, m, n):
            """
            :type m: int
            :type n: int
            :rtype: int
            """
            a=[[1 for j in range(n)] for i in range(m)]
            for i in range(1,m):
                for j in range(1,n):
                    a[i][j]=a[i-1][j]+a[i][j-1]
            return a[m-1][n-1]
                    