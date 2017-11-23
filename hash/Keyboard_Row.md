# 500. Keyboard Row

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard

    look down at your pc

Example 1:

    Input: ["Hello", "Alaska", "Dad", "Peace"]
    Output: ["Alaska", "Dad"]

Note:
- You may use one character in the keyboard more than once.
- You may assume the input string will only contain letters of alphabet.

## Method:

    class Solution(object):
        def findWords(self, words):
            """
            :type words: List[str]
            :rtype: List[str]
            """
            s1=('q','w','e','r','t','y','u','i','o','p')
            s2=('a','s','d','f','g','h','j','k','l')
            s3=('z','x','c','v','b','n','m')
            res=[]
            for word in words:
                if all(w.lower() in s1 for w in word) or all(w.lower() in s2 for w in word) or all(w.lower() in s3 for w in word):
                    res.append(word)
            return res
            
