# 213. House Robber II

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

## Method:
将环形DP问题转化为两趟线性DP问题：

    class Solution(object):
        def rob(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            if len(nums)==1:
                return nums[0]
            return max(self.linearRob(nums[1:]), self.linearRob(nums[:-1]))
            
        def linearRob(self, nums):
            if len(nums)==0:
                return 0
            dp=[0] * len(nums)
            for i in range(len(nums)):
                if i==0:
                    dp[i]=nums[0]
                elif i==1:
                    dp[i]=max(nums[0],nums[1])
                else:
                    dp[i]=max(dp[i-2]+nums[i],dp[i-1])
            return dp[-1]