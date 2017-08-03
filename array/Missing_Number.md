# 268. Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

## Method:
顺序遍历数组：(O(nlogn) time complexity）

    class Solution(object):
        def missingNumber(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            nums.sort()
            for i in range(len(nums)-1):
                if nums[i]+1!=nums[i+1]:
                    return nums[i]+1
            return nums[-1]+1 if nums[0]==0 else 0
## Solution:
利用求和公式：

    class Solution(object):
        def missingNumber(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            s = int((len(nums)+1)*len(nums)/2)
            return s-sum(nums)
利用set：(O(n) space complexity)
    
    class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        temp_set = set([i for i in range(length+1)])
        nums_set = set(nums)
        res = list(temp_set - nums_set)
        return res[0]