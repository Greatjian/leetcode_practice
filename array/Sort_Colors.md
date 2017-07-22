# 075. Sort Colors

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?

## Method:
使用三指针，前后标记0，2位置，中间依次遍历，分别判断并与前后交换位置：

注意判断条件mid<=j，且与后指针交换元素时中指针不后移。

    class Solution(object):
        def sortColors(self, nums):
            """
            :type nums: List[int]
            :rtype: void Do not return anything, modify nums in-place instead.
            """
            i,mid,j=0,0,len(nums)-1
            while mid<=j:
                if nums[mid]==0:
                    nums[i],nums[mid]=nums[mid],nums[i]
                    i+=1
                    mid+=1
                elif nums[mid]==2:
                    nums[j],nums[mid]=nums[mid],nums[j]
                    j-=1
                else:
                    mid+=1
