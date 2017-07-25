# 080. Remove Duplicates from Sorted Array II

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

## Method:
使用pop清除第三个以上的相同元素，该方法会改变数组长度，
故遍历不能用for i in range，而使用while i... i+=1

    class Solution(object):
        def removeDuplicates(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            count=0
            i=1
            while i<len(nums):
                if nums[i]==nums[i-1]:
                    count+=1
                else:
                    count=0
                if count>=2:
                    nums.pop(i)
                    i-=1
                i+=1
也可以不改变数组长度，增设一指针将第三个以上的相同元素赋值为下一不同元素值：

比较时可与前二位比较

    class Solution(object):
        def removeDuplicates(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            i = 0
            for n in nums:
                if i < 2 or n > nums[i-2]:
                    nums[i] = n
                    i += 1
            return i
