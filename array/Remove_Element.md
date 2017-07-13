## 027. Remove Element

Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

    Example:
    Given input array nums = [3,2,2,3], val = 3

    Your function should return length = 2, with the first two elements of nums being 2.

## Method:

first thought: 与前题类似，可利用双指针前后夹逼，
将非指定数字与指定数字交换并返回位置实现：

```
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j=len(nums)-1
        for i in range(len(nums)):
            while i<=j:
                while i<=j and nums[i]!=val:
                    i+=1
                while i<=j and nums[j]==val:
                    j-=1
                if i<j:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
                    j-=1
        return j+1
```

## Solution

同样是双指针，但两指针均为倒序交换元素。
```
class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        j = len(A)-1
        for i in range(len(A) - 1, -1, -1):
            if A[i] == elem:
                A[i], A[j] = A[j], A[i]
                j -= 1
        return j+1