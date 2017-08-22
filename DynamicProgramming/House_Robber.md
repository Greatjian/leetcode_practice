# 198. House Robber


You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

## Method:
dp, 寻找递推公式：

    class Solution(object):
        def rob(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            if not nums:
                return 0
            if len(nums)==1:
                return nums[0]
            if len(nums)==2:
                return max(nums[0],nums[1])
            dp=[0 * i for i in range(len(nums))]
            dp[0],dp[1]=nums[0],max(nums[0],nums[1])
            for i in range(2,len(nums)):
                dp[i]=max(dp[i-2]+nums[i],dp[i-1])
            return dp[-1]
                 
## Solution:
same

    class Solution(object):
        def rob(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            if len(nums)==0: return 0
            dp = [0]*len(nums)
            for i in range(len(nums)):
                if i==0:
                    dp[i] = nums[i]
                elif i==1:
                    dp[i] = max(dp[i-1], nums[i])
                else:
                    dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            return dp[-1]
空间复杂度O(1):

    class Solution:
        # @param num, a list of integer
        # @return an integer
        def rob(self, num):
            size = len(num)
            odd, even = 0, 0
            for i in range(size):
                if i % 2:
                    odd = max(odd + num[i], even)
                else:
                    even = max(even + num[i], odd)
            return max(odd, even)