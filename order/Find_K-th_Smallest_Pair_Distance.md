# 719. Find K-th Smallest Pair Distance

Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:

    Input:
    nums = [1,3,1]
    k = 1
    Output: 0 
    Explanation:
    Here are all the pairs:
    (1,3) -> 2
    (1,1) -> 0
    (3,1) -> 2
    Then the 1st smallest distance pair is (1,1), and its distance is 0.

Note:
- 2 <= len(nums) <= 10000.
- 0 <= nums[i] < 1000000.
- 1 <= k <= len(nums) * (len(nums) - 1) / 2.

## Method:

binary search:

    class Solution(object):
        def smallestDistancePair(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
            nums.sort()
            lo=float('inf')
            for i in range(1, len(nums)):
                lo=min(lo, nums[i]-nums[i-1])
            hi=nums[-1]-nums[0]
            while lo<hi:
                mid=(lo+hi)/2
                count=0
                j=0
                for i in range(len(nums)):
                    while j<len(nums) and nums[j]-nums[i]<=mid:
                        j+=1
                    count+=j-i-1
                if count>k-1:
                    hi=mid
                else:
                    lo=mid+1
            return lo
            
heap, tle:

    class Solution(object):
        def smallestDistancePair(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
            nums.sort()
            hp=[(nums[i]-nums[i-1], i, i-1) for i in range(1, len(nums))]
            heapq.heapify(hp)
            
            for _ in range(k):
                value, end, start=heapq.heappop(hp)
                if end+1<len(nums):
                    heapq.heappush(hp, (nums[end+1]-nums[start], end+1, start))
            return value