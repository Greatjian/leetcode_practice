# 033. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

## Method:
暴力遍历查找，时间复杂度O(n):

```
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans=-1
        for i in range(len(nums)):
            if nums[i]==target:
                ans=i
        if len(nums)==0:
            ans=-1
        return ans
```
## Solution
采用二分法，时间复杂度为：
<math xmlns="http://www.w3.org/1998/Math/MathML">  <mstyle displaystyle="true">    <msub>      <mrow>        <mi> log </mi>      </mrow>      <mrow>        <mn> 2 </mn>      </mrow>    </msub>    <mi> n </mi>  </mstyle></math>

```
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<=right:
            mid =left+(right-left)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>nums[left]:
                if nums[left]<=target<=nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            elif nums[mid]<nums[left]:
                if nums[mid]<=target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
            else:   #two numbers
                left+=1
        return -1
```