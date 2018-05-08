# 763. Partition Labels

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

    Input: S = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

- S will have length in range [1, 500].
- S will consist of lowercase letters ('a' to 'z') only.

## Method:

Two pointers:

    class Solution(object):
        def partitionLabels(self, S):
            """
            :type S: str
            :rtype: List[int]
            """
            res=[]
            d={}
            for i, v in enumerate(S):
                d[v]=i
            start, end=0, 0
            i=0
            while i<len(S):
                end=max(end, d[S[i]])
                if i==end:
                    res.append(end-start+1)
                    start=end+1
                i+=1
            return res