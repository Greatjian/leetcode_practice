# 680. Valid Palindrome II

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:

    Input: "aba"
    Output: True

Example 2:

    Input: "abca"
    Output: True
    Explanation: You could delete the character 'c'.

Note:
- The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

## Method:

O(n2), tle:

    class Solution(object):
        def validPalindrome(self, s):
            """
            :type s: str
            :rtype: bool
            """
            return any(self.helper(s[:i]+s[i+1:]) for i in range(len(s)))
            
        def helper(self, s):
            return s==s[::-1]
            
## Solution:

find the deletion point and check, O(n):

    class Solution(object):
        def validPalindrome(self, s):
            """
            :type s: str
            :rtype: bool
            """
            i, j=0, len(s)-1
            while i<j:
                if s[i]==s[j]:
                    i+=1
                    j-=1
                else:
                    break
            return s[i:j]==s[i:j][::-1] or s[i+1:j+1]==s[i+1:j+1][::-1]
            
            