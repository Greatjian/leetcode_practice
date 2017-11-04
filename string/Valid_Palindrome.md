# 125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,

    "A man, a plan, a canal: Panama" is a palindrome.
    "race a car" is not a palindrome.

Note:
- Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

## Method:

s.lower()

s.upper()

s.isalnum()

s.isalpha()

s.isnumeric()

    class Solution(object):
        def isPalindrome(self, s):
            """
            :type s: str
            :rtype: bool
            """
            ans=[]
            for i in s:
                if i.isalnum():
                    ans.append(i.lower())
            return ans==ans[::-1]

