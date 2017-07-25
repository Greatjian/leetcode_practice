# 081.Search in Rotated Sorted Array II

>Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

>Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.

## Solution
采用二分法，时间复杂度log n

解法同[Search in Rotated Sorted Array](/array/Search_in_Rotated_Sorted_Array.md)：
```
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<=right: #one number
            mid =(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>nums[left]:
                if nums[left]<=target<=nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            elif nums[mid]<nums[left]:
                if nums[mid]<=target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
            else:   #two numbers
                left+=1
        return -1
```