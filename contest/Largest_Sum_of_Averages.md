# 813. Largest Sum of Averages

We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

Example:

    Input: 
    A = [9,1,2,3,9]
    K = 3
    Output: 20

    Explanation: 
    The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
    We could have also partitioned A into [9, 1], [2], [3, 9], for example.
    That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
 

Note:

- 1 <= A.length <= 100.
- 1 <= A[i] <= 10000.
- 1 <= K <= A.length.
- Answers within 10^-6 of the correct answer will be accepted as correct.

## Solution:

average using preSum, dp:

    class Solution(object):
        def largestSumOfAverages(self, A, K):
            """
            :type A: List[int]
            :type K: int
            :rtype: float
            """
            P = [0]
            for x in A: 
                P.append(P[-1] + x)
            def average(i, j):
                return (P[j] - P[i]) / float(j - i)
    
            N = len(A)
            dp=[[float('-inf')]*(N+1) for _ in range(K+1)]
            for k in range(1, K+1):
                for i in range(1, N+1):
                    if k==1:
                        dp[1][i]=average(0, i)
                        continue
                    for j in range(i):
                        dp[k][i] = max(dp[k][i], average(j, i) + dp[k-1][j])
            return dp[K][N]
