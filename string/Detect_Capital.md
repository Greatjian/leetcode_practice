# 520. Detect Capital

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

- All letters in this word are capitals, like "USA".
- All letters in this word are not capitals, like "leetcode".
- Only the first letter in this word is capital if it has more than one letter, like "Google".
- Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:

    Input: "USA"
    Output: True

Example 2:

    Input: "FlaG"
    Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

## Method:

any(), all():

    class Solution(object):
        def detectCapitalUse(self, word):
            """
            :type word: str
            :rtype: bool
            """
            if all(i.isupper() for i in word):
                return True
            if not any(i.isupper() for i in word):
                return True
            if word[0].isupper() and not any(i.isupper() for i in word[1:]):
                return True
            return False
            
简写：

    class Solution(object):
        def detectCapitalUse(self, word):
            """
            :type word: str
            :rtype: bool
            """
            if word.isupper() or word.islower():
                return True
            if word[0].isupper() and word[1:].islower():
                return True
            return False
            
## Solution:

    class Solution(object):
        def detectCapitalUse(self, word):
            """
            :type word: str
            :rtype: bool
            """
            return word.isupper() or word.islower() or word.istitle()