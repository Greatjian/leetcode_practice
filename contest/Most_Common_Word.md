# 819. Most Common Word

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

    Example:
    
    Input: 
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    Output: "ball"
    
    Explanation: 
    "hit" occurs 3 times, but it is a banned word.
    "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
    Note that words in the paragraph are not case sensitive,
    that punctuation is ignored (even if adjacent to words, such as "ball,"), 
    and that "hit" isn't the answer even though it occurs more because it is banned.
 
Note:

- 1 <= paragraph.length <= 1000.
- 1 <= banned.length <= 100.
- 1 <= banned[i].length <= 10.
- The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
- Different words in paragraph are always separated by a space.
- There are no hyphens or hyphenated words.
- Words only consist of letters, never apostrophes or other punctuation symbols.

## Method:

select maximum each time, O(n^2):

    class Solution(object):
        def mostCommonWord(self, paragraph, banned):
            """
            :type paragraph: str
            :type banned: List[str]
            :rtype: str
            """
            s=set(banned)
            p=paragraph.split()
            for i in range(len(p)):
                if p[i][-1] in '!?\',;.':
                    p[i]=p[i][:-1]
                p[i]=str(p[i]).lower()
            c=collections.Counter(p)
            while c:
                m=max(c.values())
                if m>0:
                    for key in c:
                        if c[key]==m and key not in s:
                            return key
                        if c[key]==m:
                            c[key]=-1
            return None
            
## Solution:

sort O(nlogn):

    class Solution(object):
        def mostCommonWord(self, paragraph, banned):
            """
            :type paragraph: str
            :type banned: List[str]
            :rtype: str
            """
            s=set(banned)
            p=paragraph.split()
            for i in range(len(p)):
                if p[i][-1] in '!?\',;.':
                    p[i]=p[i][:-1]
                p[i]=str(p[i]).lower()
            c=collections.Counter(p)
            l=sorted(c.keys(), key=lambda i:c[i], reverse=True)
            for i in l:
                if i not in s:
                    return i
            return None
            
loop O(n):

string.strip() remove top and bottom:

    class Solution(object):
        def mostCommonWord(self, paragraph, banned):
            banset = set(banned)
            count = collections.Counter(
                word.strip("!?',;.") for word in paragraph.lower().split())
    
            ans, best = '', 0
            for word in count:
                if count[word] > best and word not in banset:
                    ans, best = word, count[word]
    
            return ans