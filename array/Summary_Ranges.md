# 228. Summary Ranges

Given a sorted integer array without duplicates, return the summary of its ranges.

    For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
    
    
## Method:
双指针，end移至后端点，通过判断前后端点是否一致分别加入res：

    class Solution(object):
        def summaryRanges(self, nums):
            """
            :type nums: List[int]
            :rtype: List[str]
            """
            start=end=0
            res=[]
            while start<len(nums):
                while end+1<len(nums) and nums[end]+1==nums[end+1]:
                    end+=1
                if start==end:
                    res.append(str(nums[start]))
                    start+=1
                    end+=1
                else:
                    res.append(str(nums[start])+'->'+str(nums[end]))
                    start=end+1
                    end+=1
            return res
                    
