# 583. Delete Operation for Two Strings

Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:

    Input: "sea", "eat"
    Output: 2
    Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Note:

- The length of given words won't exceed 500.
- Characters in given words can only be lower-case letters.

## Method:

删除可以不连续，不能用word1[i:j+1] in word2:

    class Solution(object):
        def minDistance(self, word1, word2):
            """
            :type word1: str
            :type word2: str
            :rtype: int
            """
            l=len(word1)
            dp=[[0]*l for _ in range(l)]
            m=0
            for i in range(l):
                for j in range(l):
                    if word1[i:j+1] in word2:
                        m=max(m, j-i+1)
            return len(word1)+len(word2)-2*m
            
## Solution:

dp

    class Solution(object):
        def minDistance(self, word1, word2):
            """
            :type word1: str
            :type word2: str
            :rtype: int
            """
            m=len(word1)
            n=len(word2)
            dp=[[0]*(n+1) for _ in range(m+1)]
            for i in range(m):
                for j in range(n):
                    dp[i+1][j+1]=max(dp[i][j+1], dp[i+1][j], dp[i][j]+(word1[i]==word2[j]))
            return m+n-2*dp[-1][-1]
            