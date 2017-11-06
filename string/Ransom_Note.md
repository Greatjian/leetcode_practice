# 383. Ransom Note

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true
    
## Method:

collections.Counter():

    class Solution(object):
        def canConstruct(self, ransomNote, magazine):
            """
            :type ransomNote: str
            :type magazine: str
            :rtype: bool
            """
            r=collections.Counter(ransomNote)
            m=collections.Counter(magazine)
            for i in r.keys():
                if i not in m or r[i]>m[i]:
                    return False
            return True
            
## Solution:

set+count:

    class Solution(object):
        def canConstruct(self, ransomNote, magazine):
            """
            :type ransomNote: str
            :type magazine: str
            :rtype: bool
            """
            for r in set(ransomNote):
                if ransomNote.count(r)>magazine.count(r):
                    return False
            return True