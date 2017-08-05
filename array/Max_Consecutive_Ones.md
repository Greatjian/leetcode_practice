# 485. Max Consecutive Ones

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:

    Input: [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s.
        The maximum number of consecutive 1s is 3.
Note:

- The input array will only contain 0 and 1.
- The length of input array is a positive integer and will not exceed 10,000

## Method:
简单动态规划，计数器：

    class Solution(object):
        def findMaxConsecutiveOnes(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            count=m=0
            for n in nums:
                if n:
                    count+=1
                    m=max(m,count)
                else:
                    count=0
            return m
            
            
    class Solution(object):
        def findMaxConsecutiveOnes(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            ans=0
            string=''.join(str(i) for i in nums)
            n=string.split('0')
            for i in n:
                ans=max(ans,len(i))
            return ans
            