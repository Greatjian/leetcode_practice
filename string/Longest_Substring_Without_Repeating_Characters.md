# 3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

- Given "abcabcbb", the answer is "abc", which the length is 3.

- Given "bbbbb", the answer is "b", with the length of 1.

- Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

## Method:

dict+一次遍历:

    class Solution(object):
        def lengthOfLongestSubstring(self, s):
            """
            :type s: str
            :rtype: int
            """
            d={}
            maxCount=0
            j=0
            for i in range(len(s)):
                if s[i] in d:
                    j=max(j, d[s[i]]+1)
                d[s[i]]=i
                maxCount=max(maxCount, i-j+1)     
            return maxCount
                    