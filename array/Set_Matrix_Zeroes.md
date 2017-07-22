# 073. Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.


Follow up:

Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

## Method:
O（m+n）实现方法：

对矩阵含有0元素的行列进行标识，后改变取值：

    class Solution(object):
        def setZeroes(self, matrix):
            """
            :type matrix: List[List[int]]
            :rtype: void Do not return anything, modify matrix in-place instead.
            """
            col,row=[],[]
                    
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j]==0:
                        if i not in col:
                            col.append(i)
                        if j not in row:
                            row.append(j)
    
            for i in col:
                for j in range(len(matrix[0])):
                    matrix[i][j]=0
                    
            for i in range(len(matrix)):
                for j in row:
                    matrix[i][j]=0

前一种方式是将行列数加入列表中，我们亦可用布尔值标识，
这样在之后改变取值时便于判断：

    class Solution:
        """
        @param matrix: A list of lists of integers
        @return: Nothing
        """
        def setZeroes(self, matrix):
            # write your code here
            if len(matrix)==0:
                return
            rownum = len(matrix)
            colnum = len(matrix[0])
            row = [False for i in range(rownum)]
            col = [False for i in range(colnum)]
            for i in range(rownum):
                for j in range(colnum):
                    if matrix[i][j] == 0:
                        row[i] = True
                        col[j] = True
            for i in range(rownum):
                for j in range(colnum):
                    if row[i] or col[j]:
                        matrix[i][j] = 0
                        
## Solution:
O（1）实现方法：

对第一行和第一列是否有0进行判断，然后对其余（m-1）行与（n-1）列是否有0判断
并表示在对应第一行与第一列位置，再讲第一行第一列中含0项进行整行整列标记，最后标记
第一行与第一列本身：

    class Solution(object):
        def setZeroes(self, matrix):
            """
            :type matrix: List[List[int]]
            :rtype: void Do not return anything, modify matrix in-place instead.
            """
            if not matrix:
                return
            
            m = len(matrix)
            n = len(matrix[0])
    
            row_zero = False
            for i in range(m):
                if matrix[i][0] == 0:
                    row_zero = True
            col_zero = False
            for j in range(n):
                if matrix[0][j] == 0:
                    col_zero = True
    
            for i in range(1, m):
                for j in range(1, n):
                    if matrix[i][j] == 0:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
    
            for i in range(1, m):
                if matrix[i][0] == 0:
                    for j in range(1, n):
                        matrix[i][j] = 0
    
            for j in range(1, n):
                if matrix[0][j] == 0:
                    for i in range(1, m):
                        matrix[i][j] = 0
    
            if col_zero:
                for j in range(n):
                    matrix[0][j] = 0
            if row_zero:
                for i in range(m):
                    matrix[i][0] = 0
