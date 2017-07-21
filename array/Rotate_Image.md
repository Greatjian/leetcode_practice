# 048. Rotate Image

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

## Method:
Not a in-place method

    class Solution(object):
        def rotate(self, matrix):
            """
            :type matrix: List[List[int]]
            :rtype: void Do not return anything, modify matrix in-place instead.
            """
            a=copy.deepcopy(matrix)
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    matrix[i][j]=a[len(matrix)-j-1][i]

To achieve in-place rotation we can do it twice by switching the value
between the elements in the matrix (only do half the switching each time):

    class Solution(object):
        def rotate(self, matrix):
            """
            :type matrix: List[List[int]]
            :rtype: void Do not return anything, modify matrix in-place instead.
            """
            for i in range(len(matrix)):
                for j in range(len(matrix[0])-i):
                    matrix[i][j],matrix[len(matrix)-1-j][len(matrix)-1-i]=matrix[len(matrix)-1-j][len(matrix)-1-i],matrix[i][j]
                    
            for i in range(len(matrix)//2):
                for j in range(len(matrix[0])):
                    matrix[i][j],matrix[len(matrix)-i-1][j]=matrix[len(matrix)-i-1][j],matrix[i][j]