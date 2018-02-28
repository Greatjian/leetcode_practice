# 308. Range Sum Query 2D - Mutable

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
- The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:

    Given matrix = [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, 2, 0, 1, 5],
      [4, 1, 0, 1, 7],
      [1, 0, 3, 0, 5]
    ]
    
    sumRegion(2, 1, 4, 3) -> 8
    update(3, 2, 2)
    sumRegion(2, 1, 4, 3) -> 10

Note:
- The matrix is only modifiable by the update function.
- You may assume the number of calls to update and sumRegion function is distributed evenly.
- You may assume that row1 ≤ row2 and col1 ≤ col2.

## Method:

    class NumMatrix(object):
    
        def __init__(self, matrix):
            """
            :type matrix: List[List[int]]
            """
            if not matrix:
                return
            self.matrix=matrix
            self.bit=[[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    self.insert(i+1, j+1, matrix[i][j])
                    
        def insert(self, i, j, val):
            while i<len(self.bit):
                col=j
                while col<len(self.bit[0]):
                    self.bit[i][col]+=val
                    col+=col&(-col)
                i+=i&(-i)
                
        def getSum(self, i, j):
            s=0
            while i:
                col=j
                while col:
                    s+=self.bit[i][col]
                    col-=col&(-col)
                i-=i&(-i)
            return s
    
        def update(self, row, col, val):
            """
            :type row: int
            :type col: int
            :type val: int
            :rtype: void
            """
            diff=val-self.matrix[row][col]
            self.matrix[row][col]=val
            self.insert(row+1, col+1, diff)
    
        def sumRegion(self, row1, col1, row2, col2):
            """
            :type row1: int
            :type col1: int
            :type row2: int
            :type col2: int
            :rtype: int
            """
            return self.getSum(row1, col1)+self.getSum(row2+1, col2+1)-self.getSum(row1, col2+1)-self.getSum(row2+1, col1)
    
    
    # Your NumMatrix object will be instantiated and called as such:
    # obj = NumMatrix(matrix)
    # obj.update(row,col,val)
    # param_2 = obj.sumRegion(row1,col1,row2,col2)