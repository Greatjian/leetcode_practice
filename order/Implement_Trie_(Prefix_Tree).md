# 208. Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Note:
- You may assume that all inputs are consist of lowercase letters a-z.

## Method:

    class TrieNode:
        def __init__(self):
            self.is_word=False
            self.children=collections.defaultdict(TrieNode)
    
    class Trie(object):
    
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.root=TrieNode()
    
        def insert(self, word):
            """
            Inserts a word into the trie.
            :type word: str
            :rtype: void
            """
            cur=self.root
            for letter in word:
                cur=cur.children[letter]
            cur.is_word=True
                
        def search(self, word):
            """
            Returns if the word is in the trie.
            :type word: str
            :rtype: bool
            """
            cur=self.root
            for letter in word:
                if cur.children.get(letter)==None:
                    return False
                cur=cur.children[letter]
            return cur.is_word
            
    
        def startsWith(self, prefix):
            """
            Returns if there is any word in the trie that starts with the given prefix.
            :type prefix: str
            :rtype: bool
            """
            cur=self.root
            for letter in prefix:
                if cur.children.get(letter)==None:
                    return False
                cur=cur.children[letter]
            return True
    
    
    # Your Trie object will be instantiated and called as such:
    # obj = Trie()
    # obj.insert(word)
    # param_2 = obj.search(word)
    # param_3 = obj.startsWith(prefix)
    
## Solution:

    class Trie(object):
    
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.root={}
    
        def insert(self, word):
            """
            Inserts a word into the trie.
            :type word: str
            :rtype: void
            """
            cur=self.root
            for letter in word:
                if letter not in cur:
                    cur[letter]={}
                cur=cur[letter]
            cur["is_word"]=True
                
        def search(self, word):
            """
            Returns if the word is in the trie.
            :type word: str
            :rtype: bool
            """
            cur=self.root
            for letter in word:
                if letter not in cur:
                    return False
                cur=cur[letter]
            return "is_word" in cur
            
    
        def startsWith(self, prefix):
            """
            Returns if there is any word in the trie that starts with the given prefix.
            :type prefix: str
            :rtype: bool
            """
            cur=self.root
            for letter in prefix:
                if letter not in cur:
                    return False
                cur=cur[letter]
            return True
    
    
    # Your Trie object will be instantiated and called as such:
    # obj = Trie()
    # obj.insert(word)
    # param_2 = obj.search(word)
    # param_3 = obj.startsWith(prefix)