# 240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

For example,

    Consider the following matrix:
    
    [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    Given target = 5, return true.
    
    Given target = 20, return false.
    
## Method:

2d binary search:

    class Solution(object):
        def searchMatrix(self, matrix, target):
            """
            :type matrix: List[List[int]]
            :type target: int
            :rtype: bool
            """
            if not matrix:
                return False
            
            m, n=len(matrix), len(matrix[0])
            
            def helper(m1, m2, n1, n2):
                if m1>m2 or n1>n2:
                    return False
                m, n=(m1+m2)/2, (n1+n2)/2
                if matrix[m][n]==target:
                    return True
                if matrix[m][n]>target:
                    return helper(m1, m-1, n1, n2) or helper(m1, m2, n1, n-1)
                else:
                    return helper(m+1, m2, n1, n2) or helper(m1, m2, n+1, n2)
                
            return helper(0, m-1, 0, n-1)
            
## Solution:

O(m+n):

    class Solution(object):
        def searchMatrix(self, matrix, target):
            """
            :type matrix: List[List[int]]
            :type target: int
            :rtype: bool
            """
            if not matrix or not matrix[0]:
                return False
            
            m, n=len(matrix), len(matrix[0])
            i, j=m-1, 0
            while i>=0 and i<m and j>=0 and j<n:
                if matrix[i][j]==target:
                    return True
                if matrix[i][j]>target:
                    i-=1
                else:
                    j+=1
            return False