# 801. Minimum Swaps To Make Sequences Increasing

We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.  (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  It is guaranteed that the given input always makes it possible.

Example:

    Input: A = [1,3,5,4], B = [1,2,3,7]
    Output: 1

Explanation: 

    Swap A[3] and B[3].  Then the sequences are:
    A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
    which are both strictly increasing.

Note:

- A, B are arrays with the same length, and that length will be in the range [1, 1000].
- A[i], B[i] are integer values in the range [0, 2000].

## Method:

greedy, fail at:

    [0,4,4,5,9]
    [0,1,6,8,10]

    class Solution(object):
        def minSwap(self, A, B):
            """
            :type A: List[int]
            :type B: List[int]
            :rtype: int
            """
            cnt=0
            for i in range(1, len(A)):
                if A[i]<=A[i-1] or B[i]<=B[i-1]:
                    A[i], B[i]=B[i], A[i]
                    cnt+=1
            return min(cnt, len(A)-cnt)
            
## Solution:

total of 2^n moves, using dp to store (natural, swap):

    class Solution(object):
        def minSwap(self, A, B):
            """
            :type A: List[int]
            :type B: List[int]
            :rtype: int
            """
            dp=[[float('inf')]*2 for _ in range(len(A))]
            dp[0][0], dp[0][1]=0, 1
            for i in range(1, len(dp)):
                if A[i]>A[i-1] and B[i]>B[i-1]:
                    dp[i][0]=min(dp[i][0], dp[i-1][0])
                    dp[i][1]=min(dp[i][1], dp[i-1][1]+1)
                if A[i]>B[i-1] and B[i]>A[i-1]:
                    dp[i][0]=min(dp[i][0], dp[i-1][1])
                    dp[i][1]=min(dp[i][1], dp[i-1][0]+1)
            return min(dp[-1])
            
change to O(1) space:

    class Solution(object):
        def minSwap(self, A, B):
            """
            :type A: List[int]
            :type B: List[int]
            :rtype: int
            """
            natural, swap=0, 1
            for i in range(1, len(A)):
                n, s=float('inf'), float('inf')
                if A[i]>A[i-1] and B[i]>B[i-1]:
                    n=min(n, natural)
                    s=min(s, swap+1)
                if A[i]>B[i-1] and B[i]>A[i-1]:
                    n=min(n, swap)
                    s=min(s, natural+1)
                natural, swap=n, s
            return min(natural, swap)