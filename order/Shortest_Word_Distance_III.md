# 245. Shortest Word Distance III

This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

    For example,
    Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
    
    Given word1 = “makes”, word2 = “coding”, return 1.
    Given word1 = "makes", word2 = "makes", return 3.

Note:
- You may assume word1 and word2 are both in the list.

## Method:

    class Solution(object):
        def shortestWordDistance(self, words, word1, word2):
            """
            :type words: List[str]
            :type word1: str
            :type word2: str
            :rtype: int
            """
            res=float('inf')
            w1, w2=-1, -1
            for i in range(len(words)):
                if words[i]==word1:
                    w1=i
                if (words[i]==word1 or words[i]==word2) and w1!=-1 and w2!=-1:
                    res=min(res, abs(w1-w2))
                if words[i]==word2:
                    w2=i
            if word1!=word2:
                res=min(res, abs(w1-w2))
            return res
            
a slight modification from first problem:

    class Solution(object):
        def shortestWordDistance(self, words, word1, word2):
            """
            :type words: List[str]
            :type word1: str
            :type word2: str
            :rtype: int
            """
            res=float('inf')
            w1, w2=-1, -1
            for i in range(len(words)):
                if words[i]==word1:
                    if word1==word2:
                        w2=w1
                    w1=i
                elif words[i]==word2:
                    w2=i
                if w1!=-1 and w2!=-1:
                    res=min(res, abs(w1-w2))
            return res