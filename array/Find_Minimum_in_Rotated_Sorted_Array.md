# 153. Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

## Solution:
二分法，注意条件与1，2number时的对应。

    class Solution(object):
        def findMin(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            left,right=0,len(nums)-1
            while left<=right: #one number
                mid=(left+right)//2
                if nums[mid]<nums[left]:
                    right=mid
                elif nums[mid]>nums[left]:
                    if nums[right]>nums[mid]>nums[left]:
                        right=mid
                    else:
                        left=mid
                else: #two numbers
                    return min(nums[left],nums[right])
                
            