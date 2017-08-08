# 643. Maximum Average Subarray I

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

    Input: [1,12,-5,-6,50,3], k = 4
    Output: 12.75

Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Note:
- 1 <= k <= n <= 30,000.
- Elements of the given array will be in the range [-10,000, 10,000].

## Method:
一次遍历，总和夹头去尾不断改变：

    class Solution(object):
        def findMaxAverage(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: float
            """
            res=s=sum(nums[0:k])
            for i in range(k,len(nums)):
                s=s+nums[i]-nums[i-k]
                res=max(res,s)
            return 1.0*res/k
            
滑动窗口：

    class Solution(object):
        def findMaxAverage(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: float
            """
            ans = None
            sums = 0
            for x in range(len(nums)):
                sums += nums[x]
                if x >= k: sums -= nums[x - k]
                if x >= k - 1: ans = max(ans, 1.0 * sums / k)
            return ans