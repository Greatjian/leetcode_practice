# 516. Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:

    Input:
    
    "bbbab"
    Output:
    4
    One possible longest palindromic subsequence is "bbbb".

Example 2:

    Input:
    
    "cbbd"
    Output:
    2
    One possible longest palindromic subsequence is "bb".
    
## Method:
dfs超时：

    class Solution(object):
        def longestPalindromeSubseq(self, s):
            """
            :type s: str
            :rtype: int
            """
            self.m=0
            l=list(s)
            self.dfs([], l)
            return self.m
            
        def isPalindrome(self, s):
            i,j=0, len(s)-1
            while i<=j:
                if s[i]!=s[j]:
                    return False
                else:
                    i+=1
                    j-=1
            return True
            
        def dfs(self, path, s):
            if self.isPalindrome(path) and path:
                if len(path)>self.m:
                    self.m=len(path)
            for i in range(len(s)):
                self.dfs(path+[s[i]], s[:i]+s[i+1:])
                
## Solution:

dp，注意i,j次序，确保dp[0][l-1]最后被更新：

    class Solution(object):
        def longestPalindromeSubseq(self, s):
            """
            :type s: str
            :rtype: int
            """
            l=len(s)
            dp=[[0]*(l) for _ in range(l)]                    
            for i in range(l-1,-1,-1):
                dp[i][i]=1
                for j in range(i+1,l):
                    if s[i]==s[j]:
                        dp[i][j]=2+dp[i+1][j-1]
                    else:
                        dp[i][j]=max(dp[i+1][j],dp[i][j-1])
            return dp[0][l-1]

将dp改为一维数组，cur不断更新下一轮：

    class Solution(object):
        def longestPalindromeSubseq(self, s):
            """
            :type s: str
            :rtype: int
            """
            l=len(s)
            dp=[0]*l
            for i in range(l-1, -1, -1):
                cur=[0]*l
                cur[i]=1
                for j in range(i+1, l):
                    if s[i]==s[j]:
                        cur[j]=dp[j-1]+2
                    else:
                        cur[j]=max(dp[j], cur[j-1])
                dp=cur
            return dp[-1]
            