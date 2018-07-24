# 418. Sentence Screen Fitting

Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

Note:

- A word cannot be split into two lines.
- The order of words in the sentence must remain unchanged.
- Two consecutive words in a line must be separated by a single space.
- Total words in the sentence won't exceed 100.
- Length of each word is greater than 0 and won't exceed 10.
- 1 ≤ rows, cols ≤ 20,000.

Example 1:

    Input:
    rows = 2, cols = 8, sentence = ["hello", "world"]
    
    Output: 
    1
    
    Explanation:
    hello---
    world---
    
    The character '-' signifies an empty space on the screen.

Example 2:

    Input:
    rows = 3, cols = 6, sentence = ["a", "bcd", "e"]
    
    Output: 
    2
    
    Explanation:
    a-bcd- 
    e-a---
    bcd-e-
    
    The character '-' signifies an empty space on the screen.

Example 3:

    Input:
    rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]
    
    Output: 
    1
    
    Explanation:
    I-had
    apple
    pie-I
    had--

    The character '-' signifies an empty space on the screen.
    
## Method:

brute force, O(rc), TLE:

    class Solution(object):
        def wordsTyping(self, sentence, rows, cols):
            """
            :type sentence: List[str]
            :type rows: int
            :type cols: int
            :rtype: int
            """
            i=0
            cnt=0
            for r in range(rows):
                col=cols
                while col>=len(sentence[i]):
                    col-=len(sentence[i])+1
                    i+=1
                    if i==len(sentence):
                        cnt+=1
                        i=0
            return cnt
            
## Solution:

O(r+len(sentence)), use dp to record next movement:

    class Solution(object):
        def wordsTyping(self, sentence, rows, cols):
            """
            :type sentence: List[str]
            :type rows: int
            :type cols: int
            :rtype: int
            """
            s=' '.join(sentence)+' '
            dp=[0]*len(s)
            for i in range(1, len(dp)):
                dp[i]=dp[i-1]-1 if s[i]!=' ' else 1
            cnt=0
            for r in range(rows):
                cnt+=cols
                cnt+=dp[cnt%len(s)]
            return cnt/len(s)