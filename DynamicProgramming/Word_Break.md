# 139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

    For example, given
    s = "leetcode",
    dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

## Method:

dfs1, time limit exceeded:

    class Solution(object):
        def wordBreak(self, s, wordDict):
            """
            :type s: str
            :type wordDict: List[str]
            :rtype: bool
            """
            res=[False]
            self.wordSearch(s,wordDict,res)
            return res[0]
    
        def wordSearch(self,s,dict,res):
            if not s:
                res[0]=True
            for i in range(len(s)):
                if s[:i+1] in dict:
                    self.wordSearch(s[i+1:],dict,res)
                    
dfs2, time limit exceeded:

    class Solution(object):
        def wordBreak(self, s, wordDict):
            """
            :type s: str
            :type wordDict: List[str]
            :rtype: bool
            """
            def backtrack(table, s):
                if s=='':
                    self.res=True
                for i in range(len(s) + 1):
                    if s[:i] in table:
                        backtrack(table, s[i:])
             
            self.res=False
            backtrack(wordDict, s)
            return self.res
            
## Solution:
dp1:

    class Solution(object):
        def wordBreak(self, s, wordDict):
            """
            :type s: str
            :type wordDict: List[str]
            :rtype: bool
            """
            n=len(s)
            dp=[False]*(n+1)
            dp[0]=True
            
            for i in range(n):
                for j in range(i+1):
                    if dp[j] and s[j:i+1] in wordDict:
                        dp[i+1]=True
                        break
            return dp[n]
            
dp2:

    class Solution(object):
        def wordBreak(self, s, wordDict):
            """
            :type s: str
            :type wordDict: List[str]
            :rtype: bool
            """
            dp = [False for _ in xrange(len(s)+1)]
            dp[0]=True
            for i in xrange(len(s)):
                for w in wordDict:
                    if s[i+1-len(w):i+1] == w and dp[i-len(w)+1] and i+1-len(w)>=0: 
                        dp[i+1] = True
                        break
            return dp[-1]