# 566. Reshape the Matrix

In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:

    Input: 
    nums = 
    [[1,2],
     [3,4]]
    r = 1, c = 4
    
    Output: 
    [[1,2,3,4]]
    
Explanation:

The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.

Example 2:

    Input: 
    nums = 
    [[1,2],
     [3,4]]
    r = 2, c = 4
    
    Output: 
    [[1,2],
     [3,4]]
     
Explanation:

There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

Note:
- The height and width of the given matrix is in range [1, 100].
- The given r and c are all positive.

## Method:
新建s记录所有元素，后依次补充至答案中，两次遍历：

    class Solution(object):
        def matrixReshape(self, nums, r, c):
            """
            :type nums: List[List[int]]
            :type r: int
            :type c: int
            :rtype: List[List[int]]
            """
            m,n=len(nums),len(nums[0])
            if m*n!=r*c:
                return nums
            s=[]
            res=[[0 for i in range(c)] for j in range(r)]
            for i in range(m):
                for j in range(n):
                    s.append(nums[i][j])
            k=0
            for i in range(r):
                for j in range(c):
                    res[i][j]=s[k]
                    k+=1
            return res

## Solution:
一次遍历，不需额外占用空间（、与%的妙用）：

    class Solution(object):
        def matrixReshape(self, nums, r, c):
            """
            :type nums: List[List[int]]
            :type r: int
            :type c: int
            :rtype: List[List[int]]
            """
            h, w = len(nums), len(nums[0])
            if h * w != r * c: return nums
            ans = []
            for x in range(r):
                row = []
                for y in range(c):
                    row.append(nums[(x * c + y) / w][(x * c + y) % w])
                ans.append(row)
            return ans

或：

    class Solution(object):
        def matrixReshape(self, nums, r, c):
            """
            :type nums: List[List[int]]
            :type r: int
            :type c: int
            :rtype: List[List[int]]
            """
            
            res = [[0 for i in range(c)] for j in range(r)]
            
            if len(nums) * len(nums[0]) != r*c:
                return nums
            
            z = 0
            for x in range(len(nums)):
                for y in range(len(nums[x])):
                    res[(z//c)][z%c] = nums[x][y]
                    z+=1
                    
            return res
            