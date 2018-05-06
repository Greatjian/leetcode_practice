# 827. Making A Large Island

In a 2D grid of 0s and 1s, we change at most one 0 to a 1.

After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).

    Example 1:
    
    Input: [[1, 0], [0, 1]]
    Output: 3
    Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:

    Input: [[1, 1], [1, 0]]
    Output: 4
    Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 1.

Example 3:

    Input: [[1, 1], [1, 1]]
    Output: 4
    Explanation: Can't change any 0 to 1, only one island with area = 1.
 

Notes:

- 1 <= grid.length = grid[0].length <= 50.
- 0 <= grid[i][j] <= 1.

## Method:

O(n^4), tle, (49/63):

    class Solution(object):
        def largestIsland(self, grid):
            """
            :type grid: List[List[int]]
            :rtype: int
            """
            res=self.getArea(grid)
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==0:
                        grid[i][j]=1
                        res=max(res, self.getArea(grid))
                        grid[i][j]=0
            return res
            
        def getArea(self, grid):
            res=0
            s=set()
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==1 and (i, j) not in s:
                        queue=collections.deque([(i, j)])
                        area=0
                        while queue:
                            x, y=queue.popleft()
                            if (x, y) not in s:
                                area+=1
                                s.add((x, y))
                                for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                                    if x+dx>=0 and y+dy>=0 and x+dx<len(grid) and y+dy<len(grid[0]) and grid[x+dx][y+dy]==1:
                                        queue.append((x+dx, y+dy))
                        res=max(res, area)
            return res
            
another idea, calculate the grid only once, O(n^2):

    class Solution(object):
        def largestIsland(self, grid):
            """
            :type grid: List[List[int]]
            :rtype: int
            """
            d=self.getArea(grid, {})
            result=0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==0:
                        res=[]
                        ans=1
                        s=set()
                        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
                            if i+di>=0 and j+dj>=0 and i+di<len(grid) and j+dj<len(grid[0]) and grid[i+di][j+dj]==1:
                                area, id=d[(i+di, j+dj)]
                                if id not in s:
                                    s.add(id)
                                    ans+=area
                        result=max(result, ans)
            return result if result!=0 else len(grid)*len(grid[0])
                                
            
        def getArea(self, grid, d):
            s=set()
            id=0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==1 and (i, j) not in s:
                        res=[]
                        queue=collections.deque([(i, j)])
                        area=0
                        id+=1
                        while queue:
                            x, y=queue.popleft()
                            if (x, y) not in s:
                                area+=1
                                s.add((x, y))
                                res.append((x, y))
                                for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                                    if x+dx>=0 and y+dy>=0 and x+dx<len(grid) and y+dy<len(grid[0]) and grid[x+dx][y+dy]==1:
                                        queue.append((x+dx, y+dy))
                        for r in res:
                            d[r]=(area, id)
            return d
            
## Solution:

grid[][]: id
area: {index: area}

    class Solution(object):
        def largestIsland(self, grid):
            """
            :type grid: List[List[int]]
            :rtype: int
            """
            m, n=len(grid), len(grid[0])
            area=collections.defaultdict(int)
            
            def dfs(i, j, id):
                ans=1
                grid[i][j]=id
                for nx, ny in neighbor(i, j):
                    if grid[nx][ny]==1:
                        ans+=dfs(nx, ny, id)
                return ans
            
            def neighbor(i, j):
                res=[]
                for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
                    if 0<=i+di<m and 0<=j+dj<n:
                        res.append((i+di, j+dj))
                return res
            
            id=2
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==1:
                        area[id]=dfs(i, j, id)
                        id+=1
            
            res=0
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==0:
                        s=set(grid[x][y] for x, y in neighbor(i, j))
                        res=max(res, 1+sum(area[k] for k in s))
            return res if res!=0 else m*n