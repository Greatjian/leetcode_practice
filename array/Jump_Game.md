# 055. Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
    
    A = [2,3,1,1,4], return true.
    
    A = [3,2,1,0,4], return false.
    
## Method:
从结尾倒序向前推进，如能到头则返回true，否则返回false。

    class Solution(object):
        def canJump(self, nums):
            """
            :type nums: List[int]
            :rtype: bool
            """ 
            target=len(nums)-1
            for i in range(len(nums)-2,-1,-1):
                if nums[i]+i>=target:
                    target=i
            if target<=0:
                return True
            return False

纪念下第一次代码一次通过！

![](/pic/first_code_direct_success.jpeg)