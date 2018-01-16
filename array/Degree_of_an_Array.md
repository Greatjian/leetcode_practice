# 697. Degree of an Array

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:

    Input: [1, 2, 2, 3, 1]
    Output: 2
    
    Explanation: 
    The input array has a degree of 2 because both elements 1 and 2 appear twice.
    Of the subarrays that have the same degree:
    [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
    The shortest length is 2. So return 2.

Example 2:

    Input: [1,2,2,3,1,4,2]
    Output: 6

Note:

- nums.length will be between 1 and 50,000.
- nums[i] will be an integer between 0 and 49,999.

## Method:

出现次数最多元素的idx差值：

    class Solution(object):
        def findShortestSubArray(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            d=collections.defaultdict(list)
            for i, v in enumerate(nums):
                d[v].append(i)
            length, m=0, 0
            for l in d.values():
                if len(l)==length:
                    m=min(m, l[-1]-l[0]+1)
                elif len(l)>length:
                    length=len(l)
                    m=l[-1]-l[0]+1
            return m