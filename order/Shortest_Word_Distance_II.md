# 244. Shortest Word Distance II

This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

    For example,
    Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
    
    Given word1 = “coding”, word2 = “practice”, return 3.
    Given word1 = "makes", word2 = "coding", return 1.

Note:
- You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

## Method:

O(n) init, O(n) search:

    class WordDistance(object):
    
        def __init__(self, words):
            """
            :type words: List[str]
            """
            self.d=collections.defaultdict(list)
            for i, v in enumerate(words):
                self.d[v].append(i)
            
        def shortest(self, word1, word2):
            """
            :type word1: str
            :type word2: str
            :rtype: int
            """
            res=float('inf')
            for a in self.d[word1]:
                for b in self.d[word2]:
                    res=min(res, abs(a-b))
            return res
    
    # Your WordDistance object will be instantiated and called as such:
    # obj = WordDistance(words)
    # param_1 = obj.shortest(word1,word2)
    
since both lists are sorted, the search function can rewrite like this:

    def shortest(self, word1, word2):
            """
            :type word1: str
            :type word2: str
            :rtype: int
            """
            res=float('inf')
            i, j=0, 0
            while i<len(self.d[word1]) and j<len(self.d[word2]):
                res=min(res, abs(self.d[word1][i]-self.d[word2][j]))
                if self.d[word1][i]<self.d[word2][j]:
                    i+=1
                else:
                    j+=1
            return res