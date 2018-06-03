# 845. Longest Mountain in Array

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

- B.length >= 3
- There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]

(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

    Input: [2,1,4,7,3,2,5]
    Output: 5
    Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:

    Input: [2,2,2]
    Output: 0
    Explanation: There is no mountain.
 
Note:

- 0 <= A.length <= 10000
- 0 <= A[i] <= 10000

## Method:

loop forwards and backwards, get the sum, defensive coding when using `max()`:

    class Solution(object):
        def longestMountain(self, A):
            """
            :type A: List[int]
            :rtype: int
            """
            l=len(A)
            left=[0]*l
            right=[0]*l
            for i in range(1, l):
                if A[i]>A[i-1]:
                    left[i]=left[i-1]+1
                else:
                    left[i]=0
            for i in range(l-2, -1, -1):
                if A[i]>A[i+1]:
                    right[i]=right[i+1]+1
                else:
                    right[i]=0
            res=0
            for i in range(l):
                if left[i] and right[i]:
                    res=max(res, left[i]+right[i]+1)
            return res