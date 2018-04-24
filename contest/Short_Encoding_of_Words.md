# 820. Short Encoding of Words

Given a list of words, we may encode it by writing a reference string S and a list of indexes A.

For example, if the list of words is ["time", "me", "bell"], we can write it as S = "time#bell#" and indexes = [0, 2, 5].

Then for each index, we will recover the word by reading from the reference string from that index until we reach a "#" character.

What is the length of the shortest reference string S possible that encodes the given words?

    Example:

    Input: words = ["time", "me", "bell"]
    Output: 10
    
    Explanation: S = "time#bell#" and indexes = [0, 2, 5].

Note:

- 1 <= words.length <= 2000.
- 1 <= words[i].length <= 7.
- Each word has only lowercase letters.

## Method:

add to set:

    class Solution(object):
        def minimumLengthEncoding(self, words):
            """
            :type words: List[str]
            :rtype: int
            """
            words.sort(key=lambda i:len(i), reverse=True)
            s=set()
            res=0
            for i in range(len(words)):
                if words[i] in s:
                    continue
                for j in range(len(words[i])):
                    s.add(words[i][j:])
                res+=len(words[i])+1
            return res
            
remove from set:

    class Solution(object):
        def minimumLengthEncoding(self, words):
            """
            :type words: List[str]
            :rtype: int
            """
            words.sort(key=lambda i:len(i), reverse=True)
            s=set(words)
            res=0
            for i in range(len(words)):
                for j in range(1, len(words[i])):
                    s.discard(words[i][j:])
            return sum(len(i)+1 for i in s)