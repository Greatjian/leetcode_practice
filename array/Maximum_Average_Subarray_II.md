# 644. Maximum Average Subarray II

Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k that has the maximum average value. And you need to output the maximum average value.

    Example 1:
    Input: [1,12,-5,-6,50,3], k = 4
    Output: 12.75
    
    Explanation:
    when length is 5, maximum average value is 10.8,
    when length is 6, maximum average value is 9.16667.
    Thus return 12.75.

Note:
- 1 <= k <= n <= 10,000.
- Elements of the given array will be in range [-10,000, 10,000].
- The answer with the calculation error less than 10-5 will be accepted.

## Method:

preSum + binary search:

    class Solution(object):
        def findMaxAverage(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: float
            """
            lo, hi=min(nums), max(nums)
            preSum=[0]*(len(nums)+1)
            while hi-lo>1e-5:
                mid=(lo+hi)*1.0/2
                for i in range(1, len(preSum)):
                    preSum[i]=preSum[i-1]+nums[i-1]-mid
                minSum, maxDiff=0, float('-inf')
                for i in range(k, len(preSum)):
                    maxDiff=max(maxDiff, preSum[i]-minSum)
                    minSum=min(minSum, preSum[i-k+1])
                if maxDiff>=0:
                    lo=mid
                else:
                    hi=mid
            return lo
                