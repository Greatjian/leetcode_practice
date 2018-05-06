# 828. Unique Letter String

A character is unique in string S if it occurs exactly once in it.

For example, in string S = "LETTER", the only unique characters are "L" and "R".

Let's define UNIQ(S) as the number of unique characters in string S.

For example, UNIQ("LETTER") =  2.

Given a string S, calculate the sum of UNIQ(substring) over all non-empty substrings of S.

If there are two or more equal substrings at different positions in S, we consider them different.

Since the answer can be very large, retrun the answer modulo 10 ^ 9 + 7.

 

Example 1:

    Input: "ABC"
    Output: 10
    Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
    Evey substring is composed with only unique letters.
    Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

Example 2:

    Input: "ABA"
    Output: 8
    Explanation: The same as example 1, except uni("ABA") = 1.
 

Note: 0 <= S.length <= 10000.

## Method:

d:{element:[idx...]}

    class Solution(object):
        def uniqueLetterString(self, S):
            """
            :type S: str
            :rtype: int
            """
            d=collections.defaultdict(list)
            for i in range(len(S)):
                d[S[i]].append(i)
            cnt=0
            for i in d.keys():
                if len(d[i])==1:
                    cnt+=(d[i][0]+1)*(len(S)-d[i][0])
                for j in range(len(d[i])):
                    if j==len(d[i])-1:
                        cnt+=(d[i][j]-d[i][j-1])*(len(S)-d[i][j])
                        continue
                    if j==0:
                        cnt+=(d[i][j]+1)*(d[i][j+1]-d[i][j])
                        continue
                    cnt+=(d[i][j]-d[i][j-1])*(d[i][j+1]-d[i][j])
            return cnt
                    
better coding style:            

    class Solution(object):
        def uniqueLetterString(self, S):
            """
            :type S: str
            :rtype: int
            """
            d=collections.defaultdict(list)
            for i in range(len(S)):
                d[S[i]].append(i)
            cnt=0
            for i in d.keys():
                for j in range(len(d[i])):
                    left=-1 if j==0 else d[i][j-1]
                    right=len(S) if j==len(d[i])-1 else d[i][j+1]
                    cnt+=(d[i][j]-left)*(right-d[i][j])
            return cnt
                    
            