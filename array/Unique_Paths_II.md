# 063. Unique Paths II

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]

The total number of unique paths is 2.

Note: m and n will be at most 100.

## Method:
数学题同上，每条路是其上方与左侧可能性之和，但需要减去障碍位置。

障碍的出现需考虑多种特殊情况。

代码实现如下：

    class Solution(object):
        def uniquePathsWithObstacles(self, obstacleGrid):
            """
            :type obstacleGrid: List[List[int]]
            :rtype: int
            """
            for i in range(len(obstacleGrid)):
                for j in range(len(obstacleGrid[0])):
                    obstacleGrid[i][j]=1-obstacleGrid[i][j]
            for i in range(len(obstacleGrid)):
                if obstacleGrid[i][0]==0 and i!=len(obstacleGrid)-1:
                    for j in range(i+1,len(obstacleGrid)):
                        obstacleGrid[j][0]=0
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[0][j]==0 and j!=len(obstacleGrid[0])-1:
                    for i in range(j+1,len(obstacleGrid[0])):
                        obstacleGrid[0][i]=0
            if not obstacleGrid[0][0]:
                    return 0
            if len(obstacleGrid)>1 and len(obstacleGrid[0])>1:
                for i in range(1,len(obstacleGrid)):
                    for j in range(1,len(obstacleGrid[0])):
                        if obstacleGrid[i][j]:
                            obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
                return obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]
            else:
                for i in range(0,len(obstacleGrid)):
                    for j in range(0,len(obstacleGrid[0])):
                        if not obstacleGrid[i][j]:
                            return 0
                return 1
      
## Solution:
相比之下更好的方式可以复制一个新数组方便操作：

    class Solution(object):
        def uniquePathsWithObstacles(self, obstacleGrid):
            """
            :type obstacleGrid: List[List[int]]
            :rtype: int
            """
            if obstacleGrid[0][0] == 1:
                return 0
            m = len(obstacleGrid)
            n = len(obstacleGrid[0])
            dp = [[0 for __ in range(n)] for __ in range(m)]
            dp[0][0] = 1
            for i in range(1, m):
                dp[i][0] = dp[i - 1][0] if obstacleGrid[i][0] == 0 else 0
            for j in range(1, n):
                dp[0][j] = dp[0][j - 1] if obstacleGrid[0][j] == 0 else 0
                
            for i in range(1, m):
                for j in range(1, n):
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            return dp[m - 1][n - 1]
            
最佳方法是建立新的一维数组，按行遍历：

    class Solution(object):
        def uniquePathsWithObstacles(self, obstacleGrid):
            """
            :type obstacleGrid: List[List[int]]
            :rtype: int
            """
            
            m = len(obstacleGrid)
            n = len(obstacleGrid[0])
            dp = [0]*n
            dp[0] = 1
            for i in range(m):
                row = obstacleGrid[i]
                for j in range(n):
                    if row[j] == 1: #obstacle
                        dp[j] = 0
                    elif j>0:
                        dp[j] += dp[j-1]
            return dp[-1]