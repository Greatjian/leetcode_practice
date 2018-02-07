# 327. Count of Range Sum

Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
- A naive algorithm of O(n2) is trivial. You MUST do better than that.

    
    Example:
    Given nums = [-2, 5, -1], lower = -2, upper = 2,
    Return 3.
    The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.
    
## Method:

rangeSum is the substraction of two preSums.

classic O(n^2), tle:

    class Solution(object):
        def countRangeSum(self, nums, lower, upper):
            """
            :type nums: List[int]
            :type lower: int
            :type upper: int
            :rtype: int
            """
            cnt=0
            for i in range(1, len(nums)):
                nums[i]+=nums[i-1]
            nums.insert(0, 0)
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[j]-nums[i]>=lower and nums[j]-nums[i]<=upper:
                        cnt+=1
            return cnt

## Solution:

mergesort and count, O(nlogn):

    class Solution(object):
        def countRangeSum(self, nums, lower, upper):
            """
            :type nums: List[int]
            :type lower: int
            :type upper: int
            :rtype: int
            """
            for i in range(1, len(nums)):
                nums[i]+=nums[i-1]
            nums.insert(0, 0)
            
            def mergesort(lo, hi):
                if hi-lo<=1:
                    return 0
                mid=(lo+hi)/2
                count=mergesort(lo, mid)+mergesort(mid, hi)
                start, end=mid, mid
                for i in range(lo, mid):
                    while start<hi and nums[start]-nums[i]<lower:
                        start+=1
                    while end<hi and nums[end]-nums[i]<=upper:
                        end+=1
                    count+=end-start
                nums[lo:hi]=sorted(nums[lo:hi])
                return count
            
            return mergesort(0, len(nums))
                    
binary indexed tree:
                      
    class Solution(object):
        def countRangeSum(self, nums, lower, upper):
            """
            :type nums: List[int]
            :type lower: int
            :type upper: int
            :rtype: int
            """
            preSum=[0]
            for i in range(len(nums)):
                preSum.append(preSum[-1]+nums[i])
            s=sorted(preSum)
            bit=[0]*(len(preSum)+1)
            
            def insert(i):
                while i<len(bit):
                    bit[i]+=1
                    i+=i&(-i)
                    
            def getSum(i):
                s=0
                while i:
                    s+=bit[i]
                    i-=i&(-i)
                return s
            
            res=0
            for p in preSum:
                res+=getSum(bisect.bisect_right(s, p-lower)) - getSum(bisect.bisect_left(s, p-upper))
                insert(bisect.bisect_right(s, p))            
            return res      