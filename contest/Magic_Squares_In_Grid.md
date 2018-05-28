# 840. Magic Squares In Grid

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

    Example 1:
    
    Input: [[4,3,8,4],
            [9,5,1,9],
            [2,7,6,2]]

    Output: 1

    Explanation: 

    The following subgrid is a 3 x 3 magic square:
    438
    951
    276
    
    while this one is not:
    384
    519
    762
    
    In total, there is only one magic square inside the given grid.

Note:

- 1 <= grid.length <= 10
- 1 <= grid[0].length <= 10
- 0 <= grid[i][j] <= 15

## Method:

brute force,

find all 5, and check each 8 surroundings:

    class Solution(object):
        def numMagicSquaresInside(self, grid):
            """
            :type grid: List[List[int]]
            :rtype: int
            """
            m, n=len(grid), len(grid[0])
            cnt=0
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==5 and i not in [0, m-1] and j not in [0, n-1]:
                        s=set()
                        flag=True
                        for di1, dj1, di2, dj2 in [[-1,-1,1,1],[-1,0,1,0],[-1,1,1,-1],[0,-1,0,1]]:
                            if grid[i+di1][j+dj1]+grid[i+di2][j+dj2]!=10 or grid[i+di1][j+dj1] in s or grid[i+di2][j+dj2] in s:
                                flag=False
                                break
                            s.add(grid[i+di1][j+dj1])
                            s.add(grid[i+di2][j+dj2])
                        if flag and s==set([1,2,3,4,6,7,8,9]):
                            cnt+=1
            return cnt
            
## Solution:

clean style:

    class Solution(object):
        def numMagicSquaresInside(self, grid):
            """
            :type grid: List[List[int]]
            :rtype: int
            """
            m, n=len(grid), len(grid[0])
            
            def magic(i, j):
                a,b,c,d,e,f,g,h,i=grid[i-1][j-1],grid[i-1][j],grid[i-1][j+1],grid[i][j-1],grid[i][j],grid[i][j+1],grid[i+1][j-1],grid[i+1][j],grid[i+1][j+1]
                return a+i==b+h==c+g==d+f==10 and sorted([a,b,c,d,e,f,g,h,i])==range(1, 10)
                
            return sum(magic(i, j) for i in range(1, m-1) for j in range(1, n-1) if grid[i][j]==5)
                    