# 015. 3Sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

    For example, given array S = [-1, 0, 1, 2, -1, -4],
    A solution set is:
    [[-1, 0, 1],[-1, -1, 2]]

## Method:

first thought: sort the list and add from the smallest triplet, 
then use certain method (two pointers) for traversal.

a time complexity of O(n^2) is needed for three variables.

Two pointers are used: i,j at left side and k at right side. 
We keep i fixed and draw j, k together each time.

```
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        i=0
        while i<len(nums)-2:
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    # ignore repeat numbers
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
                else:
                    k-=1
            i+=1
            # ignore repeat numbers
            while nums[i]==nums[i-1] and i<len(nums)-2:
                i+=1
        return res
```

## Solution

思路类似，实现时将3sum转化为2sum更为直观，省略重复部分的代码实现值得学习。

```
class Solution(object):
    '''
        题意：求数列中三个数之和为0的三元组有多少个，需去重
        暴力枚举三个数复杂度为O(N^3)
        先考虑2Sum的做法，假设升序数列a，对于一组解ai,aj, 另一组解ak,al 
        必然满足 i<k j>l 或 i>k j<l, 因此我们可以用两个指针，初始时指向数列两端
        指向数之和大于目标值时，右指针向左移使得总和减小，反之左指针向右移
        由此可以用O(N)的复杂度解决2Sum问题，3Sum则枚举第一个数O(N^2)
        使用有序数列的好处是，在枚举和移动指针时值相等的数可以跳过，省去去重部分
    '''
    def threeSum(self, nums):
        nums.sort()
        res = []
        length = len(nums)
        for i in range(0, length - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            left, right = i + 1, length - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return res
```