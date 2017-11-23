# 463. Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

    [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]
    
    Answer: 16
    Explanation: The perimeter is the 16 yellow stripes in the image below:
    
    lol
    
## Method:

check for adjacent area:

    class Solution(object):
        def islandPerimeter(self, grid):
            """
            :type grid: List[List[int]]
            :rtype: int
            """
            m, n=len(grid), len(grid[0])
            count=0
            for i in range(m):
                for j in range(n):
                    if grid[i][j]:
                        if i==0 or not grid[i-1][j]:
                            count+=1
                        if i==m-1 or not grid[i+1][j]:
                            count+=1
                        if j==0 or not grid[i][j-1]:
                            count+=1
                        if j==n-1 or not grid[i][j+1]:
                            count+=1
            return count