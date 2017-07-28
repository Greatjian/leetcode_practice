# 162. Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.


Note:
Your solution should be in logarithmic complexity.

## Method:

    class Solution(object):
        def findPeakElement(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            left,right=0,len(nums)-1
            while left<right:
                mid=(left+right)//2
                if nums[mid]<nums[mid+1]:
                    left=mid+1
                else:
                    right=mid
            return left
            
## Solution:
根据元素数目分别讨论：

    class Solution(object):
        def findPeakElement(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            start, end = 0, len(nums) - 1
            if start == end: #1 number
                return start
            if start + 1 == end: #2 numbers
                return nums.index(max(nums[start], nums[end]))
            
            while start + 1 <  end: #3 numbers
                mid = start + (end - start) / 2
                if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]: #3 numbers
                    return mid
                elif nums[mid] < nums[mid - 1]: #4 numbers
                    end = mid
                elif nums[mid] < nums[mid + 1]: #4 numbers
                    start = mid
            
            return nums.index(max(nums[start], nums[end]))

            