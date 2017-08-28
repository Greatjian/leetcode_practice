# 303. Range Sum Query - Immutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]
    
    sumRange(0, 2) -> 1
    sumRange(2, 5) -> -1
    sumRange(0, 5) -> -3
    
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

## Method:

time limit exceeded:

    class NumArray(object):
    
        def __init__(self, nums):
            """
            :type nums: List[int]
            """
            self.nums=nums
    
        def sumRange(self, i, j):
            """
            :type i: int
            :type j: int
            :rtype: int
            """
            s=0
            while i<j:
                s+=self.nums[i]
            return s
    
    
    # Your NumArray object will be instantiated and called as such:
    # obj = NumArray(nums)
    # param_1 = obj.sumRange(i,j)
    
慢：

    class NumArray(object):
    
        def __init__(self, nums):
            """
            :type nums: List[int]
            """
            self.sum=[0]*(len(nums)+1)
            for i in range(len(nums)):
                self.sum[i+1]=self.sum[i]+nums[i]
    
        def sumRange(self, i, j):
            """
            :type i: int
            :type j: int
            :rtype: int
            """
            return self.sum[j+1]-self.sum[i]
            
    
    
    # Your NumArray object will be instantiated and called as such:
    # obj = NumArray(nums)
    # param_1 = obj.sumRange(i,j)
    
## Solution:
遍历求和计算部分在init内完成，可减少每次调用函数所需时间。

最后做差可以增加一空间：

    class NumArray(object):
    
        def __init__(self, nums):
            """
            :type nums: List[int]
            """
            self.sum=[0]*(len(nums)+1)
            for i in range(len(nums)):
                self.sum[i+1]=self.sum[i]+nums[i]
    
        def sumRange(self, i, j):
            """
            :type i: int
            :type j: int
            :rtype: int
            """
            return self.sum[j+1]-self.sum[i]
            
    
    
    # Your NumArray object will be instantiated and called as such:
    # obj = NumArray(nums)
    # param_1 = obj.sumRange(i,j)