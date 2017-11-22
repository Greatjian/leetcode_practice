# 409. Longest Palindrome

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
- Assume the length of given string will not exceed 1,010.


    Example:

    Input:
    "abccccdd"
    
    Output:
    7

    Explanation:
    One longest palindrome that can be built is "dccaccd", whose length is 7.
    
## Method:

    class Solution(object):
        def longestPalindrome(self, s):
            """
            :type s: str
            :rtype: int
            """
            d=collections.Counter(s)
            res=0
            for i in d.values():
                res+=i/2
            return 2 * res + (2*res!=len(s))
            
         // res=sum([i/2 for i in d.values()])
