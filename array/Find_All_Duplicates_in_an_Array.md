# 442. Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
    
    Input:
    [4,3,2,7,8,2,3,1]
    
    Output:
    [2,3]
    
## Method:
尝试用set去除重复元素然后从list减去，但remove操作O(n)，整体O(n2)超时：

    class Solution(object):
        def findDuplicates(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            for num in list(set(nums)):
                nums.remove(num)
            return nums

## Solution:

题目关键在1 ≤ a[i] ≤ n，说明a[a[i]-1]一定存在，可将元素值视作下标取负，然后使用绝对值判断：

    class Solution(object):
        def findDuplicates(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            ans = []
            for n in nums:
                if nums[abs(n) - 1] < 0:
                    ans.append(abs(n))
                else:
                    nums[abs(n) - 1] *= -1
            return ans
            
位置交换法：调整数组至nums[i]=i+1

    class Solution(object):
        def findDuplicates(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            ans = []
            for i in range(len(nums)):
                while nums[i] and nums[i] != i + 1:
                    n = nums[i]
                    if nums[i] == nums[n - 1]:
                        ans.append(n)
                        nums[i] = 0
                    else:
                        nums[i], nums[n - 1] = nums[n - 1], nums[i]
            return ans