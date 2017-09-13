# 392. Is Subsequence

Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

    Example 1:
    s = "abc", t = "ahbgdc"
    
    Return true.
    
    Example 2:
    s = "axc", t = "ahbgdc"
    
    Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

## Method:
遍历检索count：

    class Solution(object):
        def isSubsequence(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: bool
            """
            if not s:
                return True
            j=0
            for i in t:
                if i==s[j]:
                    j+=1
                if j==len(s):
                    return True
            return False
            
利用find确认位置，减少搜索数量：

    class Solution(object):
        def isSubsequence(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: bool
            """
            if not s:
                return True
            j=0
            for i in s:
                idx=t.find(i,j)
                if idx==-1:
                    return False
                j=idx+1
            return True
            
## Solution:
deque从左侧剔除，判断空集：

    class Solution(object):
        def isSubsequence(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: bool
            """
            queue = collections.deque(s)
            for c in t:
                if not queue: return True
                if c == queue[0]:
                    queue.popleft()
            return not queue
            
            