# 816. Ambiguous Coordinates

We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we removed all commas, decimal points, and spaces, and ended up with the string S.  Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits.  Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order.  Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

Example 1:

    Input: "(123)"
    Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]

Example 2:

    Input: "(00011)"
    Output:  ["(0.001, 1)", "(0, 0.011)"]

    Explanation: 
    0.0, 00, 0001 or 00.01 are not allowed.

Example 3:

    Input: "(0123)"
    Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]

Example 4:

    Input: "(100)"
    Output: [(10, 0)]

    Explanation: 
    1.0 is not allowed.
 
Note:

- 4 <= S.length <= 12.
- S[0] = "(", S[S.length - 1] = ")", and the other elements in S are digits.

## Method:

    class Solution(object):
        def ambiguousCoordinates(self, S):
            """
            :type S: str
            :rtype: List[str]
            """
            res=[]
            s=S[1:-1]
            for i in range(len(s)-1):
                left=s[:i+1]
                right=s[i+1:]
                if len(left)==1:
                    leftans=[left]
                else:
                    leftans=[]
                    for k in range(len(left)-1):
                        nleft=left[:k+1]
                        nright=left[k+1:]
                        if nright[-1]=='0' or len(nleft)>1 and nleft[0]=='0':
                            continue
                        new=nleft+'.'+nright
                        leftans.append(new)
                    if not (len(left)>1 and left[0]=='0'):
                        leftans.append(left)
                if len(right)==1:
                    rightans=[right]
                else:
                    rightans=[]
                    for k in range(len(right)-1):
                        nleft=right[:k+1]
                        nright=right[k+1:]
                        if nright[-1]=='0' or len(nleft)>1 and nleft[0]=='0':
                            continue
                        new=nleft+'.'+nright
                        rightans.append(new)
                    if not (len(right)>1 and right[0]=='0'):
                        rightans.append(right)
                if leftans and rightans:
                    for i in leftans:
                        for j in rightans:
                            res.append('('+i+', '+j+')')
            return res
                    
better coding style:

    class Solution(object):
        def ambiguousCoordinates(self, S):
            """
            :type S: str
            :rtype: List[str]
            """
            res=[]
            s=S[1:-1]
            for i in range(len(s)-1):
                left=s[:i+1]
                right=s[i+1:]
                leftAns=self.getRes(left)
                rightAns=self.getRes(right)
                for l in leftAns:
                    for r in rightAns:
                        res.append('('+l+', '+r+')')
            return res
                
        def getRes(self, s):
            if len(s)==1:
                return [s]
            res=[]
            for k in range(len(s)-1):
                left=s[:k+1]
                right=s[k+1:]
                if right[-1]=='0' or len(left)>1 and left[0]=='0':
                    continue
                ans=left+'.'+right
                res.append(ans)
            if not (len(s)>1 and s[0]=='0'):
                res.append(s)
            return res
                    
                    
                    