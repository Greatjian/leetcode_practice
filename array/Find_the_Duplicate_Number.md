# 287. Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:

You must not modify the array (assume the array is read only). (no sort)

You must use only constant, O(1) extra space. (no map)

Your runtime complexity should be less than O(n2).

There is only one duplicate number in the array, but it could be repeated more than once.

## Method:

遍历前后对比，修改原数组不合要求：
    
    class Solution(object):
        def findDuplicate(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            nums.sort()
            for i in range(len(nums)-1):
                if nums[i]==nums[i+1]:
                    return nums[i]
二分法O(nlogn):

遍历数组，若数组中不大于n / 2的数字个数超过n / 2，则可以确定[1, n /2]范围内一定有解，
否则可以确定解落在(n / 2, n]范围内。

    class Solution(object):
        def findDuplicate(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            low, high = 1, len(nums) - 1
            while low <= high:
                mid = (low + high) >> 1
                cnt = sum(x <= mid for x in nums)
                if cnt > mid:
                    high = mid - 1
                else:
                    low = mid + 1
            return low
## Solution:

映射找环法O（n）:
value重复说明数组中index->value映射出现环路，可通过
[Floyd's Algorithm](https://zh.wikipedia.org/wiki/Floyd%E5%88%A4%E5%9C%88%E7%AE%97%E6%B3%95)
找到环路起点。

一个很好的[解释](http://blog.csdn.net/thestoryofsnow/article/details/6822576)：

    class Solution(object):
        def findDuplicate(self, nums):
            # The "tortoise and hare" step.  We start at the end of the array and try
            # to find an intersection point in the cycle.
            slow = 0
            fast = 0
        
            # Keep advancing 'slow' by one step and 'fast' by two steps until they
            # meet inside the loop.
            while True:
                slow = nums[slow]
                fast = nums[nums[fast]]
        
                if slow == fast:
                    break
        
            # Start up another pointer from the end of the array and march it forward
            # until it hits the pointer inside the array.
            finder = 0
            while True:
                slow   = nums[slow]
                finder = nums[finder]
        
                # If the two hit, the intersection index is the duplicate element.
                if slow == finder:
                    return slow