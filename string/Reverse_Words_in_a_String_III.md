# 557. Reverse Words in a String III

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space and there will not be any extra space in the string.

## Method:

    class Solution(object):
        def reverseWords(self, s):
            """
            :type s: str
            :rtype: str
            """
            res=[]
            a=s.split()
            for i in a:
                j=list(i)
                i=''.join(j[::-1])
                res+=[i]
            return ' '.join(res)

缩减1 line:

    class Solution(object):
        def reverseWords(self, s):
            """
            :type s: str
            :rtype: str
            """
            return ' '.join([''.join(list(i)[::-1]) for i in s.split()])
            
## Solution:

str 可直接[::-1]:

    class Solution(object):
        def reverseWords(self, s):
            """
            :type s: str
            :rtype: str
            """
            return ' '.join(i[::-1] for i in s.split())