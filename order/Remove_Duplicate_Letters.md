# 316. Remove Duplicate Letters

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:

    Given "bcabc"
    Return "abc"
    
    Given "cbacdcbc"
    Return "acdb"
    
## Method:

recursion:

    class Solution(object):
        def removeDuplicateLetters(self, s):
            """
            :type s: str
            :rtype: str
            """
            c=collections.Counter(s)
            idx=0
            for i in range(len(s)):
                if ord(s[i])<ord(s[idx]):
                    idx=i
                c[s[i]]-=1
                if c[s[i]]==0:
                    break
            return '' if not s else s[idx]+self.removeDuplicateLetters(s[idx+1:].replace(s[idx], ''))
            
iteration:

    class Solution(object):
        def removeDuplicateLetters(self, s):
            """
            :type s: str
            :rtype: str
            """
            stack = []
            for i, c in enumerate(s):
                if c not in stack:
                    while stack and stack[-1] > c and stack[-1] in s[i:]:
                        stack.pop()
                    stack.append(c)
            return ''.join(stack)