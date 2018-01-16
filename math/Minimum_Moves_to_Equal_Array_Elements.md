# 453. Minimum Moves to Equal Array Elements

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

    Input:
    [1,2,3]
    
    Output:
    3
    
    Explanation:
    Only three moves are needed (remember each move increments two elements):
    
    [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
    
## Method:

（n-1）个数+1相等于1个数-1，最后同时减至最小数。

    class Solution(object):
        def minMoves(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            return sum(nums)-min(nums)*len(nums)