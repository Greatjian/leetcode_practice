# 462. Minimum Moves to Equal Array Elements II

Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

    Input:
    [1,2,3]
    
    Output:
    2
    
    Explanation:
    Only two moves are needed (remember each move increments or decrements one element):
    
    [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
    
## Solution:

[Any median minimizes the sum of absolute deviations](https://math.stackexchange.com/questions/113270/the-median-minimizes-the-sum-of-absolute-deviations):

    class Solution(object):
        def minMoves2(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            a=sorted(nums)[len(nums)/2] #median
            c=0
            for i in nums:
                c+=abs(i-a)
            return c
            
            # return sum(abs(a-i) for i in nums)