# 200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

    11110
    11010
    11000
    00000
    Answer: 1

Example 2:

    11000
    11000
    00100
    00011
    Answer: 3

## Method:

dfs stack, (bfs deque similar)

    class Solution(object):
        def numIslands(self, grid):
            """
            :type grid: List[List[str]]
            :rtype: int
            """
            if not grid:
                return 0
            
            m, n=len(grid), len(grid[0])
            stack=[]
            d={}
            for i in range(m):
                for j in range(n):
                    if grid[i][j]=='1':
                        d[(i, j)]=i*n+j
                        stack.append((i, j))
                        
            while stack:
                i, j=stack.pop()
                for (di, dj) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if i+di>=0 and i+di<m and j+dj>=0 and j+dj<n and grid[i+di][j+dj]=='1':
                        d[(i+di, j+dj)]=d[(i, j)]
                        grid[i+di][j+dj]='2'
                        stack.append((i+di, j+dj))
                                            
            return len(set(d.values()))
            
## Solution:

一次遍历即可：

    class Solution(object):
        def numIslands(self, grid):
            """
            :type grid: List[List[str]]
            :rtype: int
            """
            if not grid:
                return 0
            
            m, n=len(grid), len(grid[0])
            stack=[]
            count=0
            for i in range(m):
                for j in range(n):
                    if grid[i][j]=='1':
                        stack.append((i, j))
                        count+=1
                        while stack:
                            x, y=stack.pop()
                            for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                if x+dx>=0 and x+dx<m and y+dy>=0 and y+dy<n and grid[x+dx][y+dy]=='1':
                                    grid[x+dx][y+dy]='0'
                                    stack.append((x+dx, y+dy))                                        
            return count
            
recursion:

    class Solution(object):
        def numIslands(self, grid):
            """
            :type grid: List[List[str]]
            :rtype: int
            """
            if not grid:
                return 0
            
            def dfs(i, j):
                for (di, dj) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if i+di>=0 and i+di<m and j+dj>=0 and j+dj<n and grid[i+di][j+dj]=='1':
                        grid[i+di][j+dj]='0'
                        dfs(i+di, j+dj)
                        
            m, n=len(grid), len(grid[0])
            count=0
            for i in range(m):
                for j in range(n):
                    if grid[i][j]=='1':
                        count+=1
                        dfs(i, j)                         
            return count
            
union find:
 
    class UF:
        def __init__(self, val):
            self.parent=[0]*val
            self.cnt=0
            
        def find(self, node):
            if self.parent[node]!=node:
                self.parent[node]=self.find(self.parent[node])
            return self.parent[node]
        
        def union(self, p, q):
            r1, r2=self.find(p), self.find(q)
            if r1!=r2:
                self.parent[r1]=r2
                self.cnt-=1
    
    
    class Solution(object):
        def numIslands(self, grid):
            """
            :type grid: List[List[str]]
            :rtype: int
            """
            if not grid:
                return 0
                        
            m, n=len(grid), len(grid[0])
            uf=UF(m*n)
            for i in range(m):
                for j in range(n):
                    if grid[i][j]=='1':
                        uf.parent[i*n+j]=i*n+j
                        uf.cnt+=1
                        
            for i in range(m):
                for j in range(n):
                    if grid[i][j]=='1':
                        for di, dj in [[0,-1],[0,1],[1,0],[-1,0]]:
                            if 0<=i+di<m and 0<=j+dj<n and grid[i+di][j+dj]=='1':
                                uf.union(i*n+j, (i+di)*n+(j+dj))
            return uf.cnt
                        
            

