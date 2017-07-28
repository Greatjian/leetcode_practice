# 167. Two Sum II - Input array is sorted


Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers=[2, 7, 11, 15], target=9
Output: [1,2]

## Method:
尝试用字典方式解决因数组可能存在重复元素而失败(dic has no same elements)：

    class Solution(object):
        def twoSum(self, numbers, target):
            """
            :type numbers: List[int]
            :type target: int
            :rtype: List[int]
            """
            ans={}                                           
            for i,j in enumerate(numbers):
                ans[j]=i
            for k in ans:
                if target-k in ans: #and ans[k]!=ans[target-k]
                    print [ans[k]+1,ans[target-k]+1]
                    # return [ans[k]+1,ans[target-k]+1]
            return []
        
        # [0,0,3,4],0
        # ->[2,2]
        
我们可以
    
    class Solution(object):
        def twoSum(self, numbers, target):
            """
            :type numbers: List[int]
            :type target: int
            :rtype: List[int]
            """
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num] + 1, i + 1]
            dic[num] = i

## Solution:
two pointers:

    class Solution(object):
        def twoSum(self, numbers, target):
            """
            :type numbers: List[int]
            :type target: int
            :rtype: List[int]
            """
            if len(numbers)<2:
                return None
            i,j=0,len(numbers)-1
            while i<j:
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
                elif numbers[i]+numbers[j]<target:
                    i+=1
                else:
                    j-=1
            return None

