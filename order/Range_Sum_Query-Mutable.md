# 307. Range Sum Query - Mutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

    Example:
    Given nums = [1, 3, 5]
    
    sumRange(0, 2) -> 9
    update(1, 2)
    sumRange(0, 2) -> 8

Note:
- The array is only modifiable by the update function.
- You may assume the number of calls to update and sumRange function is distributed evenly.

## Method:

using bit:

    class NumArray(object):
    
        def __init__(self, nums):
            """
            :type nums: List[int]
            """
            self.nums=nums
            self.bit=[0]*(len(nums)+1)
            for i in range(1, len(self.bit)):
                self.insert(i, nums[i-1])
            
        def insert(self, i, val):
            while i<len(self.bit):
                self.bit[i]+=val
                i+=i&(-i)
                
        def getSum(self, i):
            s=0
            while i:
                s+=self.bit[i]
                i-=i&(-i)
            return s
    
        def update(self, i, val):
            """
            :type i: int
            :type val: int
            :rtype: void
            """
            diff=val-self.nums[i]
            self.nums[i]=val
            self.insert(i+1, diff)
    
        def sumRange(self, i, j):
            """
            :type i: int
            :type j: int
            :rtype: int
            """
            return self.getSum(j+1)-self.getSum(i)
            
    # Your NumArray object will be instantiated and called as such:
    # obj = NumArray(nums)
    # obj.update(i,val)
    # param_2 = obj.sumRange(i,j)