# 041. First Missing Positive

Given an unsorted integer array, find the first missing positive integer.

For example,

    Given [1,2,0] return 3,
    and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

## Method:

swap value to the right position using index:

    class Solution(object):
        def firstMissingPositive(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            for i in range(len(nums)):
                while nums[i]-1>=0 and nums[i]-1<len(nums) and nums[i]!=nums[nums[i]-1]:
                    nums[nums[i]-1], nums[i]=nums[i], nums[nums[i]-1]
            for i in range(len(nums)):
                if nums[i]!=i+1:
                    return i+1
            return len(nums)+1