# 843. Guess the Word

This problem is an interactive problem new to the LeetCode platform.

We are given a word list of unique words, each word is 6 letters long, and one word in this list is chosen as secret.

You may call master.guess(word) to guess a word.  The guessed word should have type string and must be from the original list with 6 lowercase letters.

This function returns an integer type, representing the number of exact matches (value and position) of your guess to the secret word.  Also, if your guess is not in the given wordlist, it will return -1 instead.

For each test case, you have 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or less calls to master.guess and at least one of these guesses was the secret, you pass the testcase.

Besides the example test case below, there will be 5 additional test cases, each with 100 words in the word list.  The letters of each word in those testcases were chosen independently at random from 'a' to 'z', such that every word in the given word lists is unique.

Example 1:

    Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]

    Explanation:
    
    master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
    master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
    master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
    master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
    master.guess("abcczz") returns 4, because "abcczz" has 4 matches.

    We made 5 calls to master.guess and one of them was the secret, so we pass the test case.

Note:  Any solutions that attempt to circumvent the judge will result in disqualification.

## Method:

Guess the new word based on previous guessing result, randomly shuffle the list is important:

    # """
    # This is Master's API interface.
    # You should not implement it, or speculate about its implementation
    # """
    #class Master(object):
    #    def guess(self, word):
    #        """
    #        :type word: str
    #        :rtype int
    #        """
    
    class Solution(object):
        def findSecretWord(self, wordlist, master):
            """
            :type wordlist: List[Str]
            :type master: Master
            :rtype: None
            """
            random.shuffle(wordlist)
            l=len(wordlist)
            dp=[[-1]*l for _ in range(l)]
            for i in range(l):
                for j in range(l):
                    dp[i][j]=self.test(wordlist[i], wordlist[j])
            d={}
            for i in range(l):
                if self.match(d, dp, i):
                    d[i]=master.guess(wordlist[i])
            
        def test(self, s1, s2):
            return sum(s1[i]==s2[i] for i in range(len(s1)))
        
        def match(self, d, dp, index):
            for i, v in d.items():
                if dp[i][index]!=v:
                    return False
            return True
            
## Solution:

shorten the wordlist after randomly guessing each time:

    # """
    # This is Master's API interface.
    # You should not implement it, or speculate about its implementation
    # """
    #class Master(object):
    #    def guess(self, word):
    #        """
    #        :type word: str
    #        :rtype int
    #        """
    
    class Solution(object):
        def findSecretWord(self, wordlist, master):
            """
            :type wordlist: List[Str]
            :type master: Master
            :rtype: None
            """
            guess=0
            while guess<6:
                word=random.choice(wordlist)
                guess=master.guess(word)
                wordlist=[i for i in wordlist if self.test(i, word)==guess]
            
        def test(self, s1, s2):
            return sum(s1[i]==s2[i] for i in range(len(s1)))
            
or minimax, instead of picking randomly, we process wordlist every time such as 
we choose the word has the minimum 0 matches (more time, less guess):

    # """
    # This is Master's API interface.
    # You should not implement it, or speculate about its implementation
    # """
    #class Master(object):
    #    def guess(self, word):
    #        """
    #        :type word: str
    #        :rtype int
    #        """
    
    class Solution(object):
        def findSecretWord(self, wordlist, master):
            """
            :type wordlist: List[Str]
            :type master: Master
            :rtype: None
            """
            guess=0
            while guess<6:
                word=self.minimax(wordlist)
                guess=master.guess(word)
                wordlist=[i for i in wordlist if self.test(i, word)==guess]
            
        def test(self, s1, s2):
            return sum(s1[i]==s2[i] for i in range(len(s1)))
        
        def minimax(self, wordlist):
            c=collections.defaultdict(int)
            for w1 in wordlist:
                for w2 in wordlist:
                    if self.test(w1, w2)==0:
                        c[w1]+=1
            return min(wordlist, key=lambda i: c[i])