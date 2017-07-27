# 120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
    
    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

## Method:
初始化数组后不断更新元素值：

    class Solution(object):
        def minimumTotal(self, triangle):
            """
            :type triangle: List[List[int]]
            :rtype: int
            """
            res=[0]*len(triangle)
            for i in range(len(triangle)):
                for j in range(i,-1,-1):
                    if j==i:
                        res[j]=res[j-1]+triangle[i][i]
                    if j>0 and j<i:
                        res[j]=triangle[i][j]+min(res[j],res[j-1])
                    if j==0 and i!=0:
                        res[j]+=triangle[i][0]
            return min(res)
            # ans=res[0]
            # for element in res:
            #     if element<ans:
            #         ans=element
            # return ans
## Solution:
倒层倒序遍历更为简洁：

    class Solution(object):
        def minimumTotal(self, triangle):
            """
            :type triangle: List[List[int]]
            :rtype: int
            """
            n = len(triangle)
    
            dp = triangle[n-1]
    
            for i in range(n-2,-1,-1):
                for j in range(i+1):
                    dp[j] = min( dp[j], dp[j+1] ) + triangle[i][j]
    
            return dp[0]