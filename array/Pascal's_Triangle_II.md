# 119. Pascal's Triangle II


Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

## Solution:
直接初始化数组，为防止数值被覆盖，可倒序遍历：

    class Solution(object):
        def getRow(self, rowIndex):
            """
            :type rowIndex: int
            :rtype: List[int]
            """
            res=[1]*(rowIndex+1)
                
            for i in range(0,rowIndex-1): #level
                for j in range(i+1,0,-1): #index
                    res[j]+=res[j-1]
            return res
        
        # k=4
        # 11111
        # 12111
        # 13311
        # 14641