# 127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

For example,

    Given:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]

    As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
    return its length 5.

Note:
- Return 0 if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume beginWord and endWord are non-empty and are not the same.

UPDATE (2017/1/20):
- The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

## Method:

bfs, using deque, tle:

    class Solution(object):
        def ladderLength(self, beginWord, endWord, wordList):
            """
            :type beginWord: str
            :type endWord: str
            :type wordList: List[str]
            :rtype: int
            """
            d=collections.deque([beginWord])
            dist=2
            while d:
                for _ in range(len(d)):
                    word=d.popleft()
                    nlist=[]
                    for i in wordList:
                        if self.isSimilar(word, i):
                            if i==endWord:
                                return dist
                            d.append(i)
                        else:
                            nlist.append(i)
                    wordList=nlist
                dist+=1
            return 0
                    
        def isSimilar(self, p, q):
            diff=0
            for i in range(len(p)):
                if p[i]!=q[i]:
                    diff+=1
            return diff==1

## Solution:

set up dict to compare difference, set to check unvisited:

    class Solution(object):
        def ladderLength(self, beginWord, endWord, wordList):
            """
            :type beginWord: str
            :type endWord: str
            :type wordList: List[str]
            :rtype: int
            """
            d=collections.defaultdict(list)
            for word in wordList:
                for i in range(len(word)):
                    d[word[:i]+'_'+word[i+1:]].append(word)
            
            deque=collections.deque([beginWord])
            s=set()
            
            dist=2
            while deque:
                for _ in range(len(deque)):
                    word=deque.popleft()
                    if word not in s:
                        s.add(word)
                        for i in range(len(word)):
                            for nword in d[word[:i]+'_'+word[i+1:]]:
                                if nword==endWord:
                                    return dist
                                deque.append(nword)
                dist+=1
            return 0