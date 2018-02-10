# 266. Palindrome Permutation

Given a string, determine if a permutation of the string could form a palindrome.

    For example,
    "code" -> False, "aab" -> True, "carerac" -> True.
    
## Method:

    class Solution(object):
        def canPermutePalindrome(self, s):
            """
            :type s: str
            :rtype: bool
            """
            d=collections.Counter(s)
            count=0
            for v in d.values():
                if v%2:
                    count+=1
            return count<2