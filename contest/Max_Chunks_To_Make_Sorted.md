# 769. Max Chunks To Make Sorted

Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

    Input: arr = [4,3,2,1,0]
    Output: 1

Explanation:

    Splitting into two or more chunks will not return the required result.
    For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

Example 2:

    Input: arr = [1,0,2,3,4]
    Output: 4

Explanation:

    We can split into two chunks, such as [1, 0], [2, 3, 4].
    However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

Note:

- arr will have length in range [1, 10].
- arr[i] will be a permutation of [0, 1, ..., arr.length - 1].

## Method:

recursion, 判断前i个数最小使用了sort:

    class Solution(object):
        def maxChunksToSorted(self, arr):
            """
            :type arr: List[int]
            :rtype: int
            """
            return self.helper(0, arr)
            
        def helper(self, index, arr):
            if not arr:
                return 0
            if len(arr)==1:
                return 1
            for i in range(len(arr)):
                if sorted(arr[:i+1])==[j for j in range(index, index+i+1)]:
                    return 1+self.helper(index+i+1, arr[i+1:])
            return 1

更简单思路是：

    max(arr[:i])<min(arr[i:])
    
在下一题会遇到。