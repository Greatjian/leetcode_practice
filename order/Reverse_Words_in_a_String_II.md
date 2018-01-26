# 186. Reverse Words in a String II

Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

    For example,
    Given s = "the sky is blue",
    return "blue is sky the".

Could you do it in-place without allocating extra space?

Related problem: Rotate Array

Update (2017-10-16):
We have updated the function signature to accept a character array, 
so please reset to the default code definition by clicking on the reload button above the code editor. 
Also, Run Code is now available!

## Method:

list slicing, extra space:

    class Solution(object):
        def reverseWords(self, str):
            """
            :type str: List[str]
            :rtype: void Do not return anything, modify str in-place instead.
            """
            str.reverse()
            start=0
            for i in range(len(str)):
                if str[i]==' ':
                    str[start:i]=str[start:i][::-1]
                    start=i+1
            str[start:]=str[start:][::-1]
            
Adding new reverse function, no slicing needed, O(1) space:

    class Solution(object):
        def reverseWords(self, str):
            """
            :type str: List[str]
            :rtype: void Do not return anything, modify str in-place instead.
            """
            str.reverse()
            start=0
            for i in range(len(str)):
                if str[i]==' ':
                    self.reverse(str, start, i-1)
                    start=i+1
            self.reverse(str, start, len(str)-1)
            
        def reverse(self, str, s, e):
            while s<e:
                str[s], str[e]=str[e], str[s]
                s+=1
                e-=1