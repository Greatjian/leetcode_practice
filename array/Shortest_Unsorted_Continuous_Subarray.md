# 581. Shortest Unsorted Continuous Subarray


Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

    Example 1:
    Input: [2, 6, 4, 8, 10, 9, 15]
    Output: 5
    Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Note:
- Then length of the input array is in range [1, 10,000].
- The input array may contain duplicates, so ascending order here means <=.

## Method:
通过建立新排序数组比较：

    class Solution(object):
        def findUnsortedSubarray(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            num=sorted(nums)
            for i in range(len(nums)):
                if nums[i]!=num[i]:
                    break
                    
            for j in range(len(nums)-1,-1,-1):
                if nums[j]!=num[j]:
                    break
                    
            return j-i+1 if j!=0 else 0
            
## Solution:
从0到n-1枚举i，记满足nums[i] != snums[i]的最小i值为s，最大i值为e:

    class Solution(object):
        def findUnsortedSubarray(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            snums = sorted(nums)
            s = e = -1
            for i in range(len(nums)):
                if nums[i] != snums[i]:
                    if s == -1: s = i
                    e = i
            return e - s + 1 if e != s else 0