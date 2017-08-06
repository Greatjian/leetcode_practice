# 611. Valid Triangle Number

Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:

    Input: [2,2,3,4]
    Output: 3

Explanation:

Valid combinations are: 

    2,3,4 (using the first 2)
    2,3,4 (using the second 2)
    2,2,3

Note:

- The length of the given array won't exceed 1000.
- The integers in the given array are in the range of [0, 1000].

## Method:
三次遍历O(n^3)，超时...

    class Solution(object):
        def triangleNumber(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            nums.sort()
            count=0
            for i in range(len(nums)-2):
                if nums[i]==0:
                    continue
                for j in range(i+1,len(nums)-1):
                    k=j+1
                    while k<len(nums) and nums[i]+nums[j]>nums[k]:
                        k+=1
                        count+=1
            return count
            
将二层循环j中用k表示，超时，还是O(n^3)：

    class Solution(object):
        def triangleNumber(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            nums.sort()
            count=0
            for i in range(len(nums)-2):
                if nums[i]==0:
                    continue
                j=i+1
                k=len(nums)-1
                while j<k:
                    while nums[i]+nums[j]<=nums[k]:
                        k-=1
                    count+=k-j
                    j+=1
                    k=len(nums)-1
            return count

## Solution:
答案明显O(n^2)。与之前尝试相比，答案优点体现在双指针移动的是两小边，这样一前一后移动对不等式的影响是相反的，
故一次遍历可直接求和得出答案：

    class Solution(object):
        def triangleNumber(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            nums.sort()
            count=0
            for i in range(len(nums)):
                j=0
                k=i-1
                while j<k:
                    if nums[j]+nums[k]>nums[i]:
                        count+=k-j
                        k-=1
                    else:
                        j+=1
            return count