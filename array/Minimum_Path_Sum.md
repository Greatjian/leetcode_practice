# 064. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

## Method:
方法与前一题类似，只不过每一元素新数值为该处元素值加上上方和左侧数值的最小值。

    class Solution(object):
        def minPathSum(self, grid):
            """
            :type grid: List[List[int]]
            :rtype: int
            """
            for i in range(1,len(grid)):
                grid[i][0]+=grid[i-1][0]
            for j in range(1,len(grid[0])):
                grid[0][j]+=grid[0][j-1]
            for i in range(1,len(grid)):
                for j in range(1,len(grid[0])):
                    grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
            return grid[-1][-1]
            
## Solution:
亦可复制新数组操作，为节约空间，新数组可设置为一维：

    class Solution(object):
        def minPathSum(self, grid):
            """
            :type grid: List[List[int]]
            :rtype: int
            """
            m = len(grid)
            n = len(grid[0])
            if(m == 1 and n == 1):
                return grid[0][0]
            sum = [0 for x in range(n)]
            sum[0] = grid[0][0]
            for j in range(1, n):
                sum[j] = sum[j-1] + grid[0][j]
            for i in range(1, m):
                sum[0] += grid[i][0]
                for j in range(1, n):
                    sum[j] = min(sum[j-1], sum[j]) + grid[i][j]
            return sum[n-1]