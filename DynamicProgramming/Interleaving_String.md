# 097. Interleaving String

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,

    Given:
    s1 = "aabcc",
    s2 = "dbbca",

- When s3 = "aadbbcbcac", return true.
- When s3 = "aadbbbaccc", return false.

## Method:

    class Solution(object):
        def isInterleave(self, s1, s2, s3):
            """
            :type s1: str
            :type s2: str
            :type s3: str
            :rtype: bool
            """
            m, n, k=len(s1), len(s2), len(s3)
            if m+n!=k:
                return False
            dp=[[False]*(n+1) for _ in range(m+1)]
            dp[0][0]=True
            for i in range(1, m+1):
                dp[i][0]=dp[i-1][0] and s1[i-1]==s3[i-1]
            for j in range(1, n+1):
                dp[0][j]=dp[0][j-1] and s2[j-1]==s3[j-1]
            for i in range(1, m+1):
                for j in range(1, n+1):
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1] ) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
            return dp[-1][-1]
            
change to O(m+n) space:

    class Solution(object):
        def isInterleave(self, s1, s2, s3):
            """
            :type s1: str
            :type s2: str
            :type s3: str
            :rtype: bool
            """
            m, n, k=len(s1), len(s2), len(s3)
            if m+n!=k:
                return False
            dp=[False]*(n+1)
            dp[0]=True
            for j in range(1, n+1):
                dp[j]=dp[j-1] and s2[j-1]==s3[j-1]
            for i in range(1, m+1):
                cur=[False]*(n+1)
                cur[0]=dp[0] and s1[i-1]==s3[i-1]
                for j in range(1, n+1):
                    cur[j] = (dp[j] and s1[i-1] == s3[i+j-1] ) or (cur[j-1] and s2[j-1] == s3[i+j-1])
                dp=cur
            return dp[-1]