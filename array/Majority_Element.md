# 169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

## Solution:

超过一半且肯定存在，排序后返回中位值即可：

    class Solution(object):
        def majorityElement(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            nums.sort()
            return nums[(len(nums)-1)//2]
            
超过一半，出现该值记加一，不出现减一，返回正值结果即可：
    
    class Solution:
    
        def majorityNumber(self, nums):
            candidate = None
            count = 0
            for num in nums:
                if count == 0:
                    candidate = num
                    count += 1
                elif candidate == num:
                    count += 1
                else:
                    count -= 1
            return candidate