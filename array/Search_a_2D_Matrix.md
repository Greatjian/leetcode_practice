# 074. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

    [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    Given target = 3, return true.
    
## Method:
将矩阵每行第一个值与target比较确定若是存在的行数，
然后对该行遍历比较：

时间复杂度：O（m+n）

    class Solution(object):
        def searchMatrix(self, matrix, target):
            """
            :type matrix: List[List[int]]
            :type target: int
            :rtype: bool
            """
            if not matrix or not matrix[0]:
                return False
            if target<matrix[0][0]:
                return False
            start=0
            for i in range(1,len(matrix)):
                if matrix[i][0]>target:
                    break
                if matrix[i][0]==target:
                    return True
                else:
                    start+=1
            for j in matrix[start]:
                if j== target:
                    return True
            return False

## Solution:

可使用双指针二分法比较，一列数中第x个对应m*n矩阵中的位置可以表示为matrix[x//n][x%n]

时间复杂度：O(log2(m*n))

    class Solution(object):
        def searchMatrix(self, matrix, target):
            """
            :type matrix: List[List[int]]
            :type target: int
            :rtype: bool
            """
            if not matrix or not matrix[0]:
                return False
            m,n=len(matrix),len(matrix[0])
            lo,hi=0,m*n-1
            while lo<=hi:
                mid=(lo+hi)//2
                if matrix[mid//n][mid%n]==target:
                    return True
                elif matrix[mid//n][mid%n]>target:
                    hi=mid-1
                else:
                    lo=mid+1
            return False
            
然而方法一快...

