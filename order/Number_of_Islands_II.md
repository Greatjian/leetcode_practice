# 305. Number of Islands II

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

    Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
    Output: [1,1,2,3]
    Explanation:
    
    Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).
    
    0 0 0
    0 0 0
    0 0 0
    Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
    
    1 0 0
    0 0 0   Number of islands = 1
    0 0 0
    Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
    
    1 1 0
    0 0 0   Number of islands = 1
    0 0 0
    Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
    
    1 1 0
    0 0 1   Number of islands = 2
    0 0 0
    Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
    
    1 1 0
    0 0 1   Number of islands = 3
    0 1 0

Follow up:

- Can you do it in time complexity O(k log mn), where k is the length of the positions?

## Method:

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
        def numIslands2(self, m, n, positions):
            """
            :type m: int
            :type n: int
            :type positions: List[List[int]]
            :rtype: List[int]
            """
            res=[]
            uf=UF(m*n)
            s=set()
            for i, j in positions:
                s.add((i, j))
                uf.parent[i*n+j]=i*n+j
                uf.cnt+=1
                for di, dj in [[0,-1],[0,1],[1,0],[-1,0]]:
                    if (i+di, j+dj) in s:
                        uf.union(i*n+j, (i+di)*n+(j+dj))
                res.append(uf.cnt)
            return res