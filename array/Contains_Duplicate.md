# 217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

## Method:
1. 排序前后直接比较:
````
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True 
        return False
````
2. set比较长度

````
class Solution(object):
    def containsDuplicate(self, nums):
        copy = set(nums)
        if len(copy) < len(nums):
            return True
        return False
````
3. dict判断key是否存在
    
````
class Solution(object):
    def containsDuplicate(self, nums):
        dict = {}
        for num in nums:
            if num in dict:  
                return True
            dict[num] = 1
        return False
````