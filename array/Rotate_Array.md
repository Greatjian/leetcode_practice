# 189. Rotate Array

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

Hint:
Could you do it in-place with O(1) extra space?

## Solution:

>123456,4
>
>-->654321
>
>-->345621
>
>-->345612


    class Solution(object):
        def rotate(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: void Do not return anything, modify nums in-place instead.
            """
            k=k%len(nums)
            self.reverse(nums,0,len(nums)-1)
            # print nums
            self.reverse(nums,0,k-1)
            # print nums
            self.reverse(nums,k,len(nums)-1)
    
        def reverse(self, nums, start, end):
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
>123456,4
>
>-->345612

    class Solution(object):
        def rotate(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: void Do not return anything, modify nums in-place instead.
            """
            n=len(nums)
            k=k%n
            nums[:]=nums[n-k:]+nums[:n-k]
O(n) extra space:
>123456,4
>
>temp=3456
>
>-->123412
>
>-->345612
       
    class Solution(object):
        def rotate(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: void Do not return anything, modify nums in-place instead.
            """
            if k > len(nums):
                if len(nums)%k == 0: 
                return k = k%len(nums)
            elif k == 0:
                return
            
            rl = len(nums) - k
            tmp = nums[rl:]
            nums[k:rl+k] = nums[:rl]
            nums[:len(tmp)] = tmp