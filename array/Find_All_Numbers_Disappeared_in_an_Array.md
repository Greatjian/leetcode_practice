# 448. Find All Numbers Disappeared in an Array


Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

    Input:
    [4,3,2,7,8,2,3,1]
    
    Output:
    [5,6]

## Method:

element in list判断时间复杂度为O(n)，超时：

(element in set/dict为O(1)，但之后操作会额外占据空间)

    class Solution(object):
        def findDisappearedNumbers(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            ans=[]
            for i in range(1,len(nums)+1):
                if i not in nums:
                    ans.append(i)
            return ans

使用dict判断，但需要额外空间，不合题意：

    class Solution(object):
        def findDisappearedNumbers(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            ans=[]
            dic={}
            for n in nums:
                dic[n]=0
            for i in range(1,len(nums)+1):
                if i not in dic:
                    ans.append(i)
            return ans
            
也可使用set减法，同样需要额外空间：

    class Solution(object):
        def findDisappearedNumbers(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            s=set(i for i in range(1,len(nums)+1))
            return list(s-set(nums))
    


类似前题使用负数标记法，a[a(n)-1]一定存在：

    class Solution(object):
        def findDisappearedNumbers(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            ans=[]
            for n in nums:
                if nums[abs(n)-1]>0:
                    nums[abs(n)-1]*=-1
            for i in range(len(nums)):
                if nums[i]>0:
                    ans.append(i+1)
            return ans
            
## Solution:

简化上一版本：

    class Solution(object):
        def findDisappearedNumbers(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            for n in nums:
                #if nums[abs(n)-1]>0:
                    #nums[abs(n)-1]*=-1
                nums[abs(n)-1]=abs(nums[abs(n)-1])*(-1)
            # for i in range(len(nums)):
            #     if nums[i]>0:
            #         ans.append(i+1)
            # return ans
            return [i+1 for i, val in enumerate(nums) if val>0]
            
            
