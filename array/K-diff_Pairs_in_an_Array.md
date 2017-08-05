# 532. K-diff Pairs in an Array

Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:

    Input: [3, 1, 4, 1, 5], k = 2
    Output: 2

Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:

    Input:[1, 2, 3, 4, 5], k = 1
    Output: 4

Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:

    Input: [1, 3, 1, 5, 4], k = 0
    Output: 1

Explanation: There is one 0-diff pair in the array, (1, 1).

Note:
- The pairs (i, j) and (j, i) count as the same pair.
- The length of the array won't exceed 10,000.
- All the integers in the given input belong to the range: [-1e7, 1e7].

## Method:

使用dict的value记录key在nums中的出现次数，并分类讨论k是否为0：

    class Solution(object):
        def findPairs(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
            count=0
            # map={}
            # for num in nums:
            #     if num in map:
            #         map[num]+=1
            #     else:
            #         map[num]=1
            map = collections.Counter(nums)
            for num in map:
                if k>0:
                    if num+k in map:
                        count+=1
                elif k==0:
                    if map[num]>1:
                        count+=1
            return count

## Solution:
使用set和dict处理重复元素：

    class Solution(object):
        def findPairs(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
            if k > 0:
                return len(set(nums) & set(n + k for n in nums))
            elif k == 0:
                return sum(v > 1 for v in collections.Counter(nums).values())
            else:
                return 0