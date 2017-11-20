# 136. Single Number

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
- Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

## Method:

collections.Counter():

    class Solution(object):
        def singleNumber(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            d=collections.Counter(nums)
            for item in d:
                if d[item]==1:
                    return item
                    
## Solution:

位运算，^相同为0，相异为1，出现两次抵消：

    class Solution(object):
        def singleNumber(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            res = 0
            for i in nums:
                res ^= i
            return res
            
set():

    class Solution(object):
        def singleNumber(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            return 2*sum(set(nums))-sum(nums)