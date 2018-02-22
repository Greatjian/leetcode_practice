# 211. Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

    void addWord(word)
    bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or .. 

A . means it can represent any one letter.

For example:

    addWord("bad")
    addWord("dad")
    addWord("mad")
    search("pad") -> false
    search("bad") -> true
    search(".ad") -> true
    search("b..") -> true

Note:
- You may assume that all words are consist of lowercase letters a-z.

## Method:

dfs:

    class WordDictionary(object):
    
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.root={}
            
    
        def addWord(self, word):
            """
            Adds a word into the data structure.
            :type word: str
            :rtype: void
            """
            cur=self.root
            for letter in word:
                if letter not in cur:
                    cur[letter]={}
                cur=cur[letter]
            cur["has_word"]=True
    
        def search(self, word):
            """
            Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
            :type word: str
            :rtype: bool
            """
            cur=self.root
            
            def helper(cur, i):
                if i==len(word):
                    return "has_word" in cur
                if word[i]!='.':
                    return word[i] in cur and helper(cur[word[i]], i+1)
                else:
                    for j in cur:
                        if j!="has_word" and helper(cur[j], i+1):
                            return True
                return False
                        
            return helper(cur, 0)
    
    # Your WordDictionary object will be instantiated and called as such:
    # obj = WordDictionary()
    # obj.addWord(word)
    # param_2 = obj.search(word)
    
## Solution:

key=len, dict(list):

    class WordDictionary(object):
    
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.d=collections.defaultdict(list)
            
    
        def addWord(self, word):
            """
            Adds a word into the data structure.
            :type word: str
            :rtype: void
            """
            self.d[len(word)].append(word)
    
        def search(self, word):
            """
            Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
            :type word: str
            :rtype: bool
            """
            for w in self.d[(len(word))]:
                flag=True
                for idx, val in enumerate(word):
                    if val!='.' and w[idx]!=val:
                        flag=False
                        break
                if flag:
                    return True
            return False
    
    # Your WordDictionary object will be instantiated and called as such:
    # obj = WordDictionary()
    # obj.addWord(word)
    # param_2 = obj.search(word)