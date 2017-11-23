# 525. Contiguous Array

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

    Input: [0,1]
    Output: 2
    Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:

    Input: [0,1,0]
    Output: 2
    Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.

## Method:

后加前减：

    class Solution(object):
        def findMaxLength(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            c0, c1=0,0
            d={0:0}
            res=0
            for i in range(len(nums)):
                c0+=(nums[i]==0)
                c1+=(nums[i]==1)
                if c0-c1 in d:
                    res=max(res, i+1-d[c0-c1])
                else:
                    d[c0-c1]=i+1
            return res