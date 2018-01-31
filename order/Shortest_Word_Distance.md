# 243. Shortest Word Distance

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,

    Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
    
    Given word1 = “coding”, word2 = “practice”, return 3.
    Given word1 = "makes", word2 = "coding", return 1.

Note:
- You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

## Method:

    class Solution(object):
        def shortestDistance(self, words, word1, word2):
            """
            :type words: List[str]
            :type word1: str
            :type word2: str
            :rtype: int
            """
            res, w1, w2=float('inf'), -1, -1
            for i in range(len(words)):
                if words[i]==word1:
                    w1=i
                if words[i]==word2:
                    w2=i
                if w1!=-1 and w2!=-1:
                    diff=abs(w1-w2)
                    res=min(res, diff)
            return res