# 5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

    Input: "babad"
    
    Output: "bab"

- Note: "aba" is also a valid answer.

Example:

    Input: "cbbd"
    
    Output: "bb"
    
## Method:

考虑奇数和偶数情况：

    class Solution(object):
        def longestPalindrome(self, s):
            """
            :type s: str
            :rtype: str
            """
            self.m=0
            self.s, self.e=0, 0
            for i in range(len(s)):
                self.helper(s, i, i)
                self.helper(s, i, i+1)
            return s[self.s:self.e+1]
            
        def helper(self, s, i, j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            if j-i+1>self.m:
                self.m=j-i+1
                self.s, self.e=i+1, j-1
                
## Solution:

check for palindrom: tmp == tmp[::-1]

    class Solution(object):
        def longestPalindrome(self, s):
            """
            :type s: str
            :rtype: str
            """
            l,Max = 0,1
            for i in range(len(s)):
                tmp = s[i-Max-1 : i+1]
                if i - Max > 0 and tmp == tmp[::-1]:
                    l = i-Max-1
                    Max += 2
                    continue
                tmp = s[i-Max : i+1]
                if i-Max >= 0 and tmp == tmp[::-1]:
                    l = i-Max
                    Max += 1
            return s[l:l+Max]
    
            
                