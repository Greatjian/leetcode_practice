# 576. Out of Boundary Paths

There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.

Example 1:

    Input:m = 2, n = 2, N = 2, i = 0, j = 0
    Output: 6
    Explanation:

Example 2:

    Input:m = 1, n = 3, N = 3, i = 0, j = 1
    Output: 12
    Explanation:

Note:
- Once you move the ball out of boundary, you cannot move it back.
- The length and height of the grid is in range [1,50].
- N is in range [0,50].

## Method:
dp记录改点次数，每次移动创建ndp不断覆盖：

    class Solution(object):
        def findPaths(self, m, n, N, i, j):
            """
            :type m: int
            :type n: int
            :type N: int
            :type i: int
            :type j: int
            :rtype: int
            """
            mod=10**9+7
            dp=[[0]*(n+2) for _ in range(m+2)]
            dp[i+1][j+1]=1
            for i in range(m+2):
                dp[i][0]=-1
                dp[i][-1]=-1
            for j in range(n+2):
                dp[0][j]=-1
                dp[-1][j]=-1
            zipped=[(-1,0),(1,0),(0,-1),(0,1)]
            s=0
            for _ in range(N):
                ndp=[[0]*(n+2) for _ in range(m+2)]
                for i in range(m+2):
                    ndp[i][0]=-1
                    ndp[i][-1]=-1
                for j in range(n+2):
                    ndp[0][j]=-1
                    ndp[-1][j]=-1
                for i in range(1,m+1):
                    for j in range(1,n+1):
                        for di,dj in zipped:
                            if ndp[i+di][j+dj]!=-1:
                                ndp[i+di][j+dj]=(ndp[i+di][j+dj]+dp[i][j])%mod
                            else:
                                s=(s+dp[i][j])%mod
                dp=ndp
            return s
                
简化版：

    class Solution(object):
        def findPaths(self, m, n, N, i, j):
            """
            :type m: int
            :type n: int
            :type N: int
            :type i: int
            :type j: int
            :rtype: int
            """
            MOD = 10**9 + 7
            dz = zip((1, 0, -1, 0), (0, 1, 0, -1))
            dp = [[0] *n for x in range(m)]
            dp[i][j] = 1
            ans = 0
            for t in range(N):
                ndp = [[0] *n for x in range(m)]
                for x in range(m):
                    for y in range(n):
                        for dx, dy in dz:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n:
                                ndp[nx][ny] = (ndp[nx][ny] + dp[x][y]) % MOD
                            else:
                                ans = (ans + dp[x][y]) % MOD
                dp = ndp
            return ans
            
## Solution:
dfs+记忆化搜索：
    
    class Solution(object):
        def findPaths(self, m, n, N, i, j):
            """
            :type m: int
            :type n: int
            :type N: int
            :type i: int
            :type j: int
            :rtype: int
            """
            self.d={}
            return self.dfs(m,n,N,i,j)%(10**9+7)
            
        def dfs(self,m,n,N,i,j):
            count=0
            if N==0:
                return 0
            if (N,i,j) in self.d:
                return self.d[(N,i,j)]
            if i==0:
                count+=1
            if i==m-1:
                count+=1
            if j==0: 
                count+=1
            if j==n-1:
                count+=1
            for di,dj in zip((0,0,1,-1),(1,-1,0,0)):
                if 0<=i+di<=m-1 and 0<=j+dj<=n-1:
                    count+=self.dfs(m,n,N-1,i+di,j+dj)
            self.d[(N,i,j)]=count
            return count
            