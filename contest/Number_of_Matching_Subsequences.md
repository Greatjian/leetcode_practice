# 792. Number of Matching Subsequences

Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :

    Input: 
    S = "abcde"
    words = ["a", "bb", "acd", "ace"]
    Output: 3
    Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".

Note:

- All words in words and S will only consists of lowercase letters.
- The length of S will be in the range of [1, 50000].
- The length of words will be in the range of [1, 5000].
- The length of words[i] will be in the range of [1, 50].

## Method:

O(mn), tle:

    class Solution(object):
        def numMatchingSubseq(self, S, words):
            """
            :type S: str
            :type words: List[str]
            :rtype: int
            """
            return sum(self.isSubsequence(S, word) for word in words)
            
        def isSubsequence(self, s1, s2):
            m, n=len(s1), len(s2)
            j=0
            for i in s1:
                if j<len(s2) and s2[j]==i:
                    j+=1
                if j==len(s2):
                    return 1
            return 0
     
loop S index, O(len(S)) find:

    class Solution(object):
        def numMatchingSubseq(self, S, words):
            """
            :type S: str
            :type words: List[str]
            :rtype: int
            """
            cnt=0
            for word in words:
                idx=0
                flag=True
                for letter in word:
                    idx=S.find(letter, idx)
                    if idx==-1:
                        flag=False
                        break
                    idx+=1
                if flag:
                    cnt+=1
            return cnt
                
           
## Solution:

loop S faster, O(len(words)\*len(word)\*log(len(S))):

    class Solution(object):
        def numMatchingSubseq(self, S, words):
            """
            :type S: str
            :type words: List[str]
            :rtype: int
            """
            d=collections.defaultdict(list)
            for i in range(len(S)):
                d[S[i]].append(i)
            return sum(self.isSubsequence(d, word, 0, -1) for word in words)
            
        def isSubsequence(self, d, word, wIdx, sIdx):
            if wIdx==len(word):
                return 1
            letter=word[wIdx]
            if not d[letter] or sIdx>=d[letter][-1]:
                return 0
            idx=bisect.bisect_right(d[letter], sIdx)
            sIdx=d[letter][idx]
            return self.isSubsequence(d, word, wIdx+1, sIdx)