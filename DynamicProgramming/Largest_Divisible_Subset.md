# 368. Largest Divisible Subset

Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

    nums: [1,2,3]
    
    Result: [1,2] (of course, [1,3] will also be ok)
    
Example 2:

    nums: [1,2,4,8]
    
    Result: [1,2,4,8]

## Method:

dp状态转移方程：dp[i]=max(dp[i],dp[j]+1)

    class Solution(object):
        def largestDivisibleSubset(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            if len(nums)<=1:
                return nums
            nums.sort()
            dp=[1]*len(nums)
            ans=[None]*len(nums)
            res=[]
            for i in range(len(nums)):
                for j in range(i):
                    if nums[i]%nums[j]==0 and dp[j]+1>dp[i]:
                        dp[i]=dp[j]+1
                        ans[i]=j
            idx=dp.index(max(dp))
            while idx!=None:
                res.append(nums[idx])
                idx=ans[idx]
            return res
