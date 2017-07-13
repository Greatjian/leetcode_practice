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

## Solution
可采用指针标记非重复元素，最后返回所在位置。

```
class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if A == []:
            return 0
        count = 0
        for i in range(0, len(A)):
            if A[i] == A[i-1]:
                continue
            else:
                A[count] = A[i]
                count += 1
        return count
```
```
class Solution:
    """
    # @param A: a list of integers
    # @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        B = []
        before = None
        countb = 0
        for number in A:
            if(before != number):
                B.append(number)
                before = number
                countb = 1
            elif countb < 2:
                B.append(number)
                countb += 1
        p = 0
        for number in B:
            A[p] = number
            p += 1
        return p
```



