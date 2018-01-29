# 220. Contains Duplicate III

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

## Method:

brute force, O(nk):

    class Solution(object):
        def containsNearbyAlmostDuplicate(self, nums, k, t):
            """
            :type nums: List[int]
            :type k: int
            :type t: int
            :rtype: bool
            """
            
            if t < 0 or k <= 0 or len(nums)<=1:
                return False
            
            if t == 0 and len(nums) == len(set(nums)):
                return False
            
            n = len(nums)
            for i in range(n):
                for j in range(i+1, min(i+1+k,n)):
                    if abs(nums[j]-nums[i])<=t:
                        return True
            return False
            
## Solution:

bucket sort, O(n):

    class Solution(object):
        def containsNearbyAlmostDuplicate(self, nums, k, t):
            """
            :type nums: List[int]
            :type k: int
            :type t: int
            :rtype: bool
            """
            if t<0:
                return False
            d={}
            for i in range(len(nums)):
                m=nums[i]/(t+1)
                if m in d:
                    return True
                if m-1 in d and abs(nums[i]-d[m-1])<t+1:
                    return True
                if m+1 in d and abs(nums[i]-d[m+1])<t+1:
                    return True
                d[m]=nums[i]
                if i>=k:
                    del d[nums[i-k]/(t+1)]
            return False