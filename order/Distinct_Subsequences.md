# 115. Distinct Subsequences

Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:

    S = "rabbbit", T = "rabbit"

    Return 3.
    
## Method:

    class Solution(object):
        def numDistinct(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: int
            """
            m, n=len(s), len(t)
            dp=[[0]*(m+1) for _ in range(n+1)]
            for i in range(m+1):
                dp[0][i]=1
            for i in range(1, n+1):
                for j in range(1, m+1):
                    if s[j-1]==t[i-1]:
                        dp[i][j]=dp[i-1][j-1]+dp[i][j-1]
                    else:
                        dp[i][j]=dp[i][j-1]
            return dp[-1][-1]
            
save space:

    class Solution(object):
        def numDistinct(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: int
            """
            m, n=len(s), len(t)
            dp=[1]*(m+1)
            for i in range(1, n+1):
                cur=[0]*(m+1)
                for j in range(1, m+1):
                    cur[j]=cur[j-1]+(dp[j-1] if s[j-1]==t[i-1] else 0)
                dp=cur
            return dp[-1]