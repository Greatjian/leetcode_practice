# 315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

    Given nums = [5, 2, 6, 1]
    
    To the right of 5 there are 2 smaller elements (2 and 1).
    To the right of 2 there is only 1 smaller element (1).
    To the right of 6 there is 1 smaller element (1).
    To the right of 1 there is 0 smaller element.
    Return the array [2, 1, 1, 0].
    
## Method:

mergesort ad count, keep track of index:

    class Solution(object):
        def countSmaller(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
    
            def mergesort(s, e):
                if e-s<=1:
                    return
                mid=(s+e)/2
                mergesort(s, mid)
                mergesort(mid, e)
                j=mid
                reverse=0
                tmp=[]
                for i in range(s, mid):
                    while j<e and nums[idx[i]]>nums[idx[j]]:
                        tmp.append(idx[j])
                        j+=1
                        reverse+=1
                    tmp.append(idx[i])
                    res[idx[i]]+=reverse
                idx[s:s+len(tmp)]=tmp
            
            res=[0]*len(nums)
            idx=[i for i in range(len(nums))]
            mergesort(0, len(nums))
            return res
            
binary indexed tree:

    class Solution(object):
        def countSmaller(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            d={v:i+1 for i, v in enumerate(sorted(nums))}
            bit=[0]*(len(nums)+1)
            
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

            res=[]
            for num in reversed(nums):
                res.append(getSum(d[num]-1))
                insert(d[num])
            return res[::-1]
            
bisect-bit:

    class Solution(object):
        def countSmaller(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            s=sorted(nums)
            res=[]
            bit=[0]*(len(nums)+1)
            
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
            
            for num in reversed(nums):
                res.append(getSum(bisect.bisect_left(s, num)))
                insert(bisect.bisect_right(s, num))
            return res[::-1]