# 561. Array Partition I

Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:

    Input: [1,4,3,2]

    Output: 4

Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

Note:
- n is a positive integer, which is in the range of [1, 10000].
- All the integers in the array will be in the range of [-10000, 10000].

## Method:

排序后将数组下标为偶数的元素求和即是，时间复杂度O(nlogn):

    class Solution(object):
        def arrayPairSum(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            nums.sort()
            ans=0
            for i in range(0,len(nums)-1,2):
                ans+=nums[i]
            return ans
或者  

            return sum(sorted(nums)[::2])