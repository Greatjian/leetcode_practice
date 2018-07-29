# 737. Sentence Similarity II

Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

- The length of words1 and words2 will not exceed 1000.
- The length of pairs will not exceed 2000.
- The length of each pairs[i] will be 2.
- The length of each words[i] and pairs[i][j] will be in the range [1, 20].

## Method:

union find, with node class and dict:

    class Node:
        def __init__(self):
            self.parent=self
            self.rank=0
    
    class Solution(object):
        def areSentencesSimilarTwo(self, words1, words2, pairs):
            """
            :type words1: List[str]
            :type words2: List[str]
            :type pairs: List[List[str]]
            :rtype: bool
            """
            def find(node):
                if node.parent!=node:
                    node.parent=find(node.parent)
                return node.parent
            
            def union(p, q):
                r1, r2=find(p), find(q)
                if r1!=r2:
                    if r1.rank<r2.rank:
                        r1.parent=r2
                    elif r1.rank>r2.rank:
                        r2.parent=r1
                    else:
                        r1.parent=r2
                        r2.rank+=1
            
            d={}
            if len(words1)!=len(words2):
                return False
            for i, j in pairs:
                if i not in d:
                    d[i]=Node()
                if j not in d:
                    d[j]=Node()
                union(d[i], d[j])
            for i in range(len(words1)):
                if words1[i]==words2[i]:
                    continue
                if words1[i] not in d or words2[i] not in d:
                    return False
                if find(d[words1[i]])!=find(d[words2[i]]):
                    return False
            return True
            
dfs, build graph first and dfs each check:

    class Solution(object):
        def areSentencesSimilarTwo(self, words1, words2, pairs):
            """
            :type words1: List[str]
            :type words2: List[str]
            :type pairs: List[List[str]]
            :rtype: bool
            """
            def dfs(start, end, visited):
                visited.add(start)
                if start==end:
                    return True
                for nei in d[start]:
                    if nei not in visited:
                        if dfs(nei, end, visited):
                            return True
                return False
            
            d=collections.defaultdict(set)
            for i, j in pairs:
                d[i].add(j)
                d[j].add(i)
                
            if len(words1)!=len(words2):
                return False
            for i in range(len(words1)):
                if words1[i]==words2[i]:
                    continue
                if words1[i] not in d or words2[i] not in d:
                    return False
                if not dfs(words1[i], words2[i], set()):
                    return False
            return True