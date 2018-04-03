# 128. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,

    Given [100, 4, 200, 1, 3, 2],
    The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

## Method:

    class Solution(object):
        def longestConsecutive(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            s=set(nums)
            maxCnt=0
            for i in s:
                if i-1 not in s:
                    cnt=1
                    while i+1 in s:
                        i+=1
                        cnt+=1
                    maxCnt=max(maxCnt, cnt)
            return maxCnt