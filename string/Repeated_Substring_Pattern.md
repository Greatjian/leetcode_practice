# 459. Repeated Substring Pattern

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:

    Input: "abab"
    
    Output: True
    
    Explanation: It's the substring "ab" twice.

Example 2:

    Input: "aba"
    
    Output: False

Example 3:

    Input: "abcabcabcabc"
    
    Output: True
    
    Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

## Method:

O(n2):

    class Solution(object):
        def repeatedSubstringPattern(self, s):
            """
            :type s: str
            :rtype: bool
            """
            for i in range(1, len(s)/2+1):
                if s[i]==s[0]:
                    if s==s[:i]*(len(s)/i):
                        return True
            return False
            
## Solution:

O(n):

    class Solution(object):
        def repeatedSubstringPattern(self, s):
            """
            :type s: str
            :rtype: bool
            """
            return s in (2*s)[1:-1]