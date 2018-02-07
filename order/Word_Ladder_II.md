# 126. Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

For example,

    Given:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    Return
      [
        ["hit","hot","dot","dog","cog"],
        ["hit","hot","lot","log","cog"]
      ]

Note:
- Return an empty list if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume beginWord and endWord are non-empty and are not the same.

UPDATE (2017/1/20):
- The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

## Method:

采用1的方法，但同一层不能直接加入set，需要nset缓冲。

dict中(key, value)的储存很值得学习：

    class Solution(object):
        def findLadders(self, beginWord, endWord, wordList):
            """
            :type beginWord: str
            :type endWord: str
            :type wordList: List[str]
            :rtype: List[List[str]]
            """
            d=collections.defaultdict(list)
            for word in wordList:
                for i in range(len(word)):
                    d[word[:i]+'_'+word[i+1:]].append(word)
            
            deque=collections.deque([[beginWord]])
            s=set()
            res=[]
            flag=False
            while deque:
                snew=set()
                for _ in range(len(deque)):
                    path=deque.popleft()
                    word=path[-1]
                    if word not in s:
                        snew.add(word)
                        for i in range(len(word)):
                            for nword in d[word[:i]+'_'+word[i+1:]]:
                                if nword==endWord:
                                    res.append(path+[nword])
                                    flag=True
                                deque.append(path+[nword])
                s|=snew
                if flag:
                    return res
            return []
            
## Solution:

范例答案，bfs get distance, dfs informed search:

    class Solution(object):
        def findLadders(self, beginWord, endWord, wordList):
            """
            :type beginWord: str
            :type endWord: str
            :type wordList: List[str]
            :rtype: List[List[str]]
            """
            wordList.append(beginWord)
            neighbors=self.build_neighbors(wordList)
            # find the distance between each word in dict and endWord
            distance=self.bfs(endWord, beginWord, neighbors)
            
            res=[]
            self.dfs(neighbors, distance, beginWord, endWord, [], res)
            return res
        
        def dfs(self, neighbors, distance, start, end, path, res):
            if start==end:
                res.append(path+[start])
                return         
            for i in range(len(start)):
                s=start[:i]+'_'+start[i+1:]
                for neigh in neighbors[s]:
                    if neigh in distance and distance[neigh]==distance[start]-1:
                        self.dfs(neighbors, distance, neigh, end, path+[start], res)
        
        def build_neighbors(self, wordList):
                d=collections.defaultdict(list)
                for word in wordList:
                    for i in range(len(word)):
                        s=word[:i]+'_'+word[i+1:]
                        d[s].append(word)           
                return d
            
        def bfs(self,start,end,neighbors):
            distance=collections.defaultdict(int)
            distance[start]=0
            queue=collections.deque([start])
            
            while queue:
                word=queue.popleft()
                for i in range(len(word)):
                    s=word[:i]+'_'+word[i+1:]                        
                    for neigh in neighbors[s]:     
                        if neigh not in distance:
                            distance[neigh]=distance[word]+1
                            queue.append(neigh)
            return distance
