# 085. Maximal Rectangle


Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0

Return 6.

## Method:

similar to [Largest_Rectangle_in_Histogram](/divide_and_conquer/Largest_Rectangle_in_Histogram.md):

    class Solution(object):
        def maximalRectangle(self, matrix):
            """
            :type matrix: List[List[str]]
            :rtype: int
            """
            if not matrix:
                return 0
            m, n=len(matrix), len(matrix[0])
            height=[0]*(n+1)
            area=0
            for i in range(m):
                stack=[]
                for j in range(n+1):
                    if j<n and matrix[i][j]=='1':
                        height[j]+=1
                    else:
                        height[j]=0
                    while stack and height[stack[-1]]>height[j]:
                        top=stack.pop()
                        area=max(area, height[top]*(j-stack[-1]-1 if stack else j))
                    stack.append(j)
            return area
                