# 229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

## Method:

    class Solution(object):
        def majorityElement(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            if not nums:
                return nums
            dict={}
            count=0
            nums.sort()
            res=[]
            for i in range(len(nums)):
                if nums[i] in dict:
                    count+=1
                else:
                    dict[nums[i]]=i
                    count=1
                if count>len(nums)//3 and nums[i] not in res:
                    res.append(nums[i])
            return res
                
改良：将dict中的value值作为count，遍历时使用set:

    class Solution(object):
        def majorityElement(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            a={}
            for num in nums:
                if num in a:
                    a[num]+=1
                else:
                    a[num]=1
            l=len(nums)
            b = []
            s = set(nums)
            for i in s:
                if a[i]>l/3:
                    b.append(i)
            return b
## Solution:
最多返回两个值，分别记录数值与出现次数：

    class Solution(object):
        def majorityElement(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            if not nums:
                return []
            
            e1, c1, e2, c2 = 0, 0, 0, 0
            for n in nums:
                if n == e1:
                    c1 += 1
                elif n =    = e2:
                    c2 += 1
                elif c1 == 0:
                    e1, c1 = n , 1
                elif c2 == 0:
                    e2, c2 = n, 1
                else:
                    c1 -= 1
                    c2 -= 1
                # print e1, c1, e2, c2
            
            res = []
            if nums.count(e1) > len(nums) // 3:
                res.append(e1)
            if nums.count(e2) > len(nums) // 3:
                res.append(e2)
            return list(set(res))