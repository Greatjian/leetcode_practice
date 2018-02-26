# 727. Minimum Window Subsequence

Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

    Input: 
    S = "abcdebdde", T = "bde"
    Output: "bcde"

Explanation: 

    "bcde" is the answer because it occurs before "bdde" which has the same length.
    "deb" is not a smaller window because the elements of T in the window must occur in order.

Note:

- All the strings in the input will only contain lowercase letters.
- The length of S will be in the range [1, 20000].
- The length of T will be in the range [1, 100].

## Method:

dp[i][j] stores the starting index of array T and S with length i, j:

    class Solution(object):
        def minWindow(self, S, T):
            """
            :type S: str
            :type T: str
            :rtype: str
            """
            m, n=len(T), len(S)
            dp=[[0]*(n+1) for _ in range(m+1)]
            for i in range(n+1):
                dp[0][i]=i+1
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if T[i-1]==S[j-1]:
                        dp[i][j]=dp[i-1][j-1]
                    else:
                        dp[i][j]=dp[i][j-1]
            start, end, length=0, 0, float('inf')
            for i in range(n+1):
                if dp[-1][i]!=0 and i-dp[-1][i]<length:
                    start, end=dp[-1][i]-1, i
                    length=i-dp[-1][i]
            return S[start:end]