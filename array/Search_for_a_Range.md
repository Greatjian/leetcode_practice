# 034. Search for a Range

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,

    Given [5, 7, 7, 8, 8, 10] and target value 8,
    return [3, 4].
    
## Method:
遍历查找，时间复杂度O(n),注意特殊情况：

```
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=0
        r=len(nums)-1
        if nums==[] or nums[l]>target or nums[r]<target:
            return [-1,-1]
        while l<=r:
            if nums[l]<target:
                l+=1
            if nums[r]>target:
                r-=1
            if nums[l]>=target and nums[r]<=target:
                break
        if nums[l]==nums[r]==target:
            return [l,r]
        else:
            return [-1,-1]
        
```

## Solution

题目要求O(log n)，故应该使用二分法：

左边界标志为中间数字为目标数字，且其前面数字不存在或不是目标数字；
右边界标志为中间数字为目标数字，且其后面数字不存在或不是目标数字。

若未发现左边界则不存在目标数字。

```
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[]
        l=0
        r=len(nums)
        if nums==[]:
            return [-1,-1]
        while l<r:
            mid=(l+r)//2
            if nums[mid]==target and(mid==0 or nums[mid-1]!=target):
                res.append(mid)
                break
            if nums[mid]<target:
                l=mid+1
            if nums[mid]>=target:
                r=mid
        if res==[]:
            return [-1,-1]
        
        
        r=len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]==target and(mid==len(nums)-1 or nums[mid+1]!=target):
                res.append(mid)
                break
            if nums[mid]<=target:
                l=mid+1
            if nums[mid]>target:
                r=mid
        return res
```