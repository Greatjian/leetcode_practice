# 414. Third Maximum Number

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

    Example 1:
    Input: [3, 2, 1]

>Output: 1

Explanation: The third maximum is 1.

    Example 2:
    Input: [1, 2]

>Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

    Example 3:
    Input: [2, 2, 3, 1]

>Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

## Method:
一次遍历通过三个指针不断代替求得：

    class Solution(object):
        def thirdMax(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            a=b=c=None
            for n in nums:
                if n>a:
                    a,b,c=n,a,b
                elif a>n>b:
                    b,c=n,b
                elif b>n>c:
                    c=n
            return c if c is not None else a
## Solution:

用set去除重复元素，然后剔除两个最大值：

    class Solution(object):
        def thirdMax(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            nums = set(nums)
            if len(nums) < 3:
                return max(nums)
            nums.remove(max(nums))
            nums.remove(max(nums))
            return max(nums)