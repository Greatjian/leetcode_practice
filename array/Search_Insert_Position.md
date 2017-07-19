# 035. Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.

    [1,3,5,6], 5 → 2
    [1,3,5,6], 2 → 1
    [1,3,5,6], 7 → 4
    [1,3,5,6], 0 → 0
    
## Method:
遍历查找，时间复杂度O(n)：

```
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            elif nums[i]>target:
                return i
        return len(nums)
```

## Solution

二分法O(log n)显然更佳：

几点注意：
r=len(nums), l<r, +-1时考虑端点情况
```
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        r=len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid
                if nums[mid]<target and (mid==len(nums)-1 or nums[mid+1]>target):
                    return mid+1
            else:
                r=mid
                if nums[mid]>target and (mid==0 or nums[mid-1]<target):
                    return mid
```