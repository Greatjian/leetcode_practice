# 072. Edit Distance

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

    a) Insert a character
    b) Delete a character
    c) Replace a character
    
## Method:

similar to [lcs](https://www.geeksforgeeks.org/longest-common-subsequence/):

zero and base case

time O(mn), space O(mn):

    class Solution(object):
        def minDistance(self, word1, word2):
            """
            :type word1: str
            :type word2: str
            :rtype: int
            """
            m, n=len(word1), len(word2)
            dp=[[0]*(n+1) for _ in range(m+1)]
            for i in range(m+1):
                dp[i][0]=i
            for j in range(n+1):
                dp[0][j]=j
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if word1[i-1]==word2[j-1]:
                        dp[i][j]=dp[i-1][j-1]
                    else:
                        dp[i][j]=1+min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
            return dp[-1][-1]
            
space can reduce to O(m/n):

    dp[i][j]=dp[i-1][j-1]
    dp[i][j]=1+min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
    
    class Solution(object):
        def minDistance(self, word1, word2):
            """
            :type word1: str
            :type word2: str
            :rtype: int
            """
            m, n=len(word1), len(word2)
            dp=[i for i in range(n+1)]
            for i in range(1, m+1):
                cur=[0]*(n+1)
                cur[0]=i
                for j in range(1, n+1):
                    if word1[i-1]==word2[j-1]:
                        cur[j]=dp[j-1]
                    else:
                        cur[j]=min(cur[j-1], dp[j], dp[j-1])+1
                dp=cur
            return dp[-1]