# 283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

## Method:
remove and append:

    class Solution(object):
        def moveZeroes(self, nums):
            """
            :type nums: List[int]
            :rtype: void Do not return anything, modify nums in-place instead.
            """
            count=0
            while 0 in nums:
                nums.remove(0)
                count+=1
            nums+=count*[0]
## Solution:
1，零与非零交换位置：

    class Solution(object):
        def moveZeroes(self, nums):
            """
            :type nums: List[int]
            :rtype: void Do not return anything, modify nums in-place instead.
            """
            zero = 0 
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i], nums[zero] = nums[zero], nums[i]
                    zero += 1
2，非零覆盖零位，赋值剩余位置为零：    
    

    class Solution(object):
        def moveZeroes(self, nums):
            """
            :type nums: List[int]
            :rtype: void Do not return anything, modify nums in-place instead.
            """
            i = 0
            for n in nums:
                if n != 0:
                    nums[i] = n
                    i += 1
            for j in range(i, len(nums)):
                nums[j] = 0