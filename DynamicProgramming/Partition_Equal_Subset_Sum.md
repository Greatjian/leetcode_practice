# 416. Partition Equal Subset Sum

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.

Example 1:
    
    Input: [1, 5, 11, 5]
    
    Output: true

    Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
    
    Input: [1, 2, 3, 5]
    
    Output: false

    Explanation: The array cannot be partitioned into equal sum subsets.

## Method:
dp记录遍历数组时记录所有可能值，为防止前对后影响，赋值时可采用倒序：

    class Solution(object):
        def canPartition(self, nums):
            """
            :type nums: List[int]
            :rtype: bool
            """
            if sum(nums)%2:
                return False
            dp=[0]*(sum(nums)/2+1)
            dp[0]=1
            for num in nums:
                for i in range(len(dp)-num-1,-1,-1):
                    if dp[i]:
                        dp[i+num]=1
            return dp[-1]>0