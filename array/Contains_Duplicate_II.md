# 219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

## Method:

1. 用dict判断key是否存在：

```
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict={}
        for i in range(len(nums)):
            if nums[i] in dict:
                if abs(dict[nums[i]]-i)<=k:
                    return True 
            dict[nums[i]]=i
        return False
```
简写：
```
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False
```
2. 用value排序后比较index差值：

```
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        SoInd =sorted(range(len(nums)), key=lambda k: nums[k])        
        for i in range(0,len(SoInd)-1):
            if SoInd[i+1] - SoInd[i]<=k and nums[SoInd[i+1]] == nums[SoInd[i]]:
                return True
        return False
```