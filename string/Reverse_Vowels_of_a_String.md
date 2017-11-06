# 345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

    Given s = "hello", return "holle".

Example 2:

    Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

## Method:

two pointers:

to check contains for O(1), we can use dict or set:

    class Solution(object):
        def reverseVowels(self, s):
            """
            :type s: str
            :rtype: str
            """
            l=list(s)
            d={'a':1, 'e':1, 'i':1, 'o':1, 'u':1}
            i, j=0, len(l)-1
            while i<j:
                while l[i].lower() not in d and i<j:
                    i+=1
                while l[j].lower() not in d and i<j:
                    j-=1
                if i<j:
                    l[i], l[j]=l[j], l[i]
                    i+=1
                    j-=1
            return ''.join(l)