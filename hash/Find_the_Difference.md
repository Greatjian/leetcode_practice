# 389. Find the Difference

Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

    Example:

    Input:
    s = "abcd"
    t = "abcde"
    
    Output:
    e
    
    Explanation:
    'e' is the letter that was added.
    
## Method:

dict1() - dict2():

    class Solution(object):
        def findTheDifference(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: str
            """
            d=collections.Counter(t)-collections.Counter(s)
            return ''.join(d.elements())