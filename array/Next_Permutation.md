# 031. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
    
    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
    
## Method:
举例尝试找规律：
    
    143641--144136
    
实现方法为倒序寻找第一减小位（3），与倒序第一大于该数位（4）交换，
后部分升序排列（交换后后部分必为降序，故前后颠倒即可）

    143641--144631--144136
    
最后考虑特殊情况：
倒序时无降序位---直接前后颠倒即可

## Solution

```
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index1=index2=0
        for i in range(len(nums)-1, 0, -1):
            if nums[i]>nums[i-1]:
                index1=i-1
                break
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>nums[index1]:
                index2=i
                break
        nums[index1],nums[index2]=nums[index2],nums[index1]
        if index1==index2==0:   #倒序时无降序位
            nums.reverse()
        else:
            nums[index1+1:]=reversed(nums[index1+1:])
```