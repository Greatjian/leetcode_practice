# 026. Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, 
with the first two elements of nums being 1 and 2 respectively. 
It doesn't matter what you leave beyond the new length.

## Method:

first thought: 使用list.remove清除重复元素，但遍历时很容易out of range
```
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = 0
    for i in range(1, len(nums)):
        while a<len(nums)-1:
            if nums[i] == nums[a]:
                nums.remove(nums[i])
            else:
                a += 1
    return len(nums)
```
后发现直接遍历与前一项对比即可返回数值，
但数组非重复元素需要移至最前。
```
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                a += 1
        return len(nums)-a
```

## Solution
采用双指针，一个标记初始位置递增，另一个标记非重复元素，两指针元素通过后者赋值给前者实现。

```
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i]!= nums[i-1]:
                nums[count] = nums[i]
                count += 1
        return count
```
```
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for n in nums:
            if i<1 or n> nums[i - 1]:
                nums[i]=n
                i+=1
        return i
```



