# 809. Expressive Words

Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  Here, we have groups, of adjacent letters that are all the same character, and adjacent characters to the group are different.  A group is extended if that group is length 3 or more, so "e" and "o" would be extended in the first example, and "i" would be extended in the second example.  As another example, the groups of "abbcccaaaa" would be "a", "bb", "ccc", and "aaaa"; and "ccc" and "aaaa" are the extended groups of that string.

For some given string S, a query word is stretchy if it can be made to be equal to S by extending some groups.  Formally, we are allowed to repeatedly choose a group (as defined above) of characters c, and add some number of the same character c to it so that the length of the group is 3 or more.  Note that we cannot extend a group of size one like "h" to a group of size two like "hh" - all extensions must leave the group extended - ie., at least 3 characters long.

Given a list of query words, return the number of words that are stretchy. 

Example:

    Input: 
    S = "heeellooo"
    words = ["hello", "hi", "helo"]
    Output: 1
    Explanation: 
    We can extend "e" and "o" in the word "hello" to get "heeellooo".
    We can't extend "helo" to get "heeellooo" because the group "ll" is not extended.

Notes:

- 0 <= len(S) <= 100.
- 0 <= len(words) <= 100.
- 0 <= len(words[i]) <= 100.
- S and all words in words consist only of lowercase letters

## Method:

string manipulation, two pointers and count:

    class Solution(object):
        def expressiveWords(self, S, words):
            """
            :type S: str
            :type words: List[str]
            :rtype: int
            """
            res=0
            for word in words:
                i, j=0, 0
                flag=True
                while i<len(word) and j<len(S):
                    if word[i]!=S[j]:
                        flag=False
                        break
                    iCount, jCount=1, 1
                    while i+1<len(word) and word[i+1]==word[i]:
                        i+=1
                        iCount+=1
                    while j+1<len(S) and S[j+1]==S[j]:
                        j+=1
                        jCount+=1
                    if (jCount<3 and jCount!=iCount) or iCount>jCount:
                        flag=False
                        break
                    i+=1
                    j+=1
                if flag and i==len(word) and j==len(S):
                    res+=1
            return res
            
similar idea, no need to check for flag:

    class Solution(object):
        def expressiveWords(self, S, words):
            """
            :type S: str
            :type words: List[str]
            :rtype: int
            """
            res=0
            for word in words:
                i, j=0, 0
                while True:
                    if word[i]!=S[j]:
                        break
                    iCount, jCount=1, 1
                    while i+1<len(word) and word[i+1]==word[i]:
                        i+=1
                        iCount+=1
                    while j+1<len(S) and S[j+1]==S[j]:
                        j+=1
                        jCount+=1
                    if (jCount<3 and jCount!=iCount) or iCount>jCount:
                        break
                    i+=1
                    j+=1
                    if i==len(word) and j==len(S):
                        res+=1
                        break
                    if i==len(word) or j==len(S):
                        break
            return res