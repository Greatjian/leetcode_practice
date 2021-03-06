# 001. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
    
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

## Method

using dictionary for each element.


first try:

```
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a={}
        for i in range(len(nums)):
            a[nums[i]] = i
            #a:{2:0,7:1,11:2,15:3}
        for i in range(len(nums)):
            if target-nums[i] in a:
                if a[target-nums[i]]<=i:
                    return [a[target-nums[i]], i]
        return [-1,-1]
        
Error: case of [3,3],6 and [3,2,4],6
```

time complexity: O(n)

first judge, then add elements

## Solution:

```
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i in range(len(nums)):
            if target-nums[i] in d:
                return [d[target-nums[i]], i]
            d[nums[i]]=i
        return [-1, -1]
             
```
