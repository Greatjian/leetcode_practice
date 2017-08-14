# 131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

    For example, given s = "aab",
    Return
    
    [
      ["aa","b"],
      ["a","a","b"]
    ]

## Method:

判断回文数：s[0:i+1]==s[i::-1]，196ms:

    class Solution(object):
        def partition(self, s):
            """
            :type s: str
            :rtype: List[List[str]]
            """
            res=[]
            self.dfs(s,[],res)
            return res
            
        def dfs(self,s,path,res):
            if not len(s):
                res.append(path)
                return
            for i in range(len(s)):
                if s[0:i+1]==s[i::-1]:
                    self.dfs(s[i+1:],path+[s[0:i+1]],res)
                    
将判断回文数部分用函数形式替换，169ms：

    class Solution(object):
        def partition(self, s):
            """
            :type s: str
            :rtype: List[List[str]]
            """
            res=[]
            self.dfs(s,[],res)
            return res
            
        def dfs(self,s,path,res):
            if not len(s):
                res.append(path)
                return
            for i in range(len(s)):
                if self.isPalindrome(s[0:i+1]):
                    self.dfs(s[i+1:],path+[s[0:i+1]],res)
                    
        def isPalindrome(self, s):
            if s[:]==s[::-1]:
                return True