# 344. Reverse String

Write a function that takes a string as input and returns the string reversed.

Example:

    Given s = "hello", return "olleh".
    
## Method:

    class Solution(object):
        def reverseString(self, s):
            """
            :type s: str
            :rtype: str
            """
            return s[::-1]
            
## Solution:

    class SolutionRecursive(object):
        def reverseString(self, s):
            l = len(s)
            if l < 2:
                return s
            return self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])
    
    
    class SolutionClassic(object):
        def reverseString(self, s):
            r = list(s)
            i, j  = 0, len(r) - 1
            while i < j:
                r[i], r[j] = r[j], r[i]
                i += 1
                j -= 1
            return "".join(r)
    
    class SolutionPythonic(object):
        def reverseString(self, s):
            return s[::-1]