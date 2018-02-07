# 493. Reverse Pairs

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

    Input: [1,3,2,3,1]
    Output: 2

Example2:

    Input: [2,4,3,5,1]
    Output: 3

Note:
- The length of the given array will not exceed 50,000.
- All the numbers in the input array are in the range of 32-bit integer.

## Method:

mergesort and count:

    class Solution(object):
        def reversePairs(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            def mergesort(s, e):
                if e-s<=1:
                    return 0
                mid=(s+e)/2
                cnt=mergesort(s, mid)+mergesort(mid, e)
                j=mid
                for i in range(s, mid):
                    while j<e and nums[i]>2*nums[j]:
                        j+=1
                    cnt+=j-mid
                nums[s:e]=sorted(nums[s:e])
                return cnt
            
            return mergesort(0, len(nums))
            
binary indexed tree:

    class Solution(object):
        def reversePairs(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            s=sorted(nums+[2*num+1 for num in nums])
            bit=[0]*(len(s)+1)
            
            def insert(i):
                while i:
                    bit[i]+=1
                    i-=i&(-i)
                    
            def getSum(i):
                s=0
                while i<len(bit):
                    s+=bit[i]
                    i+=i&(-i)
                return s
            
            res=0
            for num in nums:
                res+=getSum(bisect.bisect_right(s, 2*num+1))
                insert(bisect.bisect_right(s, num))
            return res                