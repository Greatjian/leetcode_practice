# 778. Swim in Rising Water

On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:
    
    Input: [[0,2],[1,3]]
    Output: 3
    Explanation:
    At time 0, you are in grid location (0, 0).
    You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

    You cannot reach point (1, 1) until time 3.
    When the depth of water is 3, we can swim anywhere inside the grid.

Example 2:

    Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    Output: 16
    Explanation:
     0  1  2  3  4
    24 23 22 21  5
    12 13 14 15 16
    11 17 18 19 20
    10  9  8  7  6
    
    The final route is marked in bold.
    We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

Note:

- 2 <= N <= 50.
- grid[i][j] is a permutation of [0, ..., N*N - 1].

## Method:

等效转换题意很重要：

tle1, O(n^3):

    class Solution(object):
        def swimInWater(self, grid):
            """
            :type grid: List[List[int]]
            :rtype: int
            """
            d={}
            m, n=len(grid), len(grid[0])
            for i in range(m):
                for j in range(n):
                    d[grid[i][j]]=(i,j)
            for t in range(m*n-1, -1, -1):
                i, j=d[t]
                grid[i][j]=-1
                if not self.isValid(grid):
                    return t
            
            
        def isValid(self, grid):
            if grid[0][0]==-1:
                return False
            m, n=len(grid), len(grid[0])
            newgrid=[[0 for i in range(n)] for j in range(m)]
            for i in range(m):
                for j in range(n):
                    newgrid[i][j]=grid[i][j]
            queue=collections.deque([(0, 0)])
            while queue:
                i, j=queue.popleft()
                if i==m-1 and j==n-1:
                    return True
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    if i+di>=0 and i+di<m and j+dj>=0 and j+dj<n and newgrid[i+di][j+dj]!=-1:
                        queue.append((i+di, j+dj))
                        newgrid[i+di][j+dj]=-1
            return False
            
tle2:

    class Solution(object):
        def swimInWater(self, grid):
            """
            :type grid: List[List[int]]
            :rtype: int
            """
            m, n=len(grid), len(grid[0])
            res=m*n
            stack=[[[(0, 0)], grid[0][0]]]
            while stack:
                path, value=stack.pop()
                # if res!=m*n and value>res:
                #     continue
                i, j=path[-1][0], path[-1][1]
                if i==m-1 and j==n-1:
                    res=min(res, value)
                    continue
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    if i+di>=0 and i+di<m and j+dj>=0 and j+dj<n and (i+di, j+dj) not in path:
                        nvalue=max(value, grid[i+di][j+dj])
                        stack.append([path+[(i+di, j+dj)], nvalue])
            return res

## Solution:

O(n^2logn):

min-heap:

    class Solution(object):
        def swimInWater(self, grid):
            """
            :type grid: List[List[int]]
            :rtype: int
            """
            m, n=len(grid), len(grid[0])
            hp=[[grid[0][0], 0, 0]]
            res=-1
            s=set([(0, 0)])
            while hp:
                v, i, j=heapq.heappop(hp)
                res=max(res, v)
                if i==m-1 and j==n-1:
                    return res
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    if 0<=i+di<m and 0<=j+dj<n and (i+di, j+dj) not in s:
                        s.add((i+di, j+dj))
                        heapq.heappush(hp, [grid[i+di][j+dj], i+di, j+dj])
                        
bfs/dfs(faster)+binary search:

    class Solution(object):
        def swimInWater(self, grid):
            """
            :type grid: List[List[int]]
            :rtype: int
            """
            m, n=len(grid), len(grid[0])
            
            def isValid(t):
                s=set([(0, 0)])
                queue=collections.deque([(0, 0)])
                while queue:
                    i, j=queue.popleft()
                    if i==m-1 and j==n-1:
                        return True
                    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        if 0<=i+di<m and 0<=j+dj<n and grid[i+di][j+dj]<=t and (i+di, j+dj) not in s:
                            queue.append((i+di, j+dj))
                            s.add((i+di, j+dj))
                return False
            
            lo, hi = grid[0][0], m*n
            while lo<hi:
                mid=(lo+hi)/2
                if isValid(mid):
                    hi=mid
                else:
                    lo=mid+1
            return lo