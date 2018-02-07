# 777. Swap Adjacent in LR String

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

    Example:

    Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
    Output: True
    
    Explanation:
    We can transform start to end following these steps:
    RXXLRXRXL ->
    XRXLRXRXL ->
    XRLXRXRXL ->
    XRLXXRRXL ->
    XRLXXRRLX

Note:

- 1 <= len(start) = len(end) <= 10000.
- Both start and end will only consist of characters in {'L', 'R', 'X'}.

## Method:

contest passed but failed for the test case "RL" and "LR":

    class Solution(object):
        def canTransform(self, start, end):
            """
            :type start: str
            :type end: str
            :rtype: bool
            """
            if collections.Counter(start)!=collections.Counter(end):
                return False
            sr, sl, er, el=0, 0, 0, 0
            for i in range(len(start)):
                if start[i]=='R':
                    sr+=1
                elif start[i]=='L':
                    sl+=1
                if end[i]=='R':
                    er+=1
                elif end[i]=='L':
                    el+=1
                if er>sr or sl>el:
                    return False
            return True

## Solution:

    class Solution(object):
        def canTransform(self, start, end):
            """
            :type start: str
            :type end: str
            :rtype: bool
            """
            if collections.Counter(start)!=collections.Counter(end):
                return False
            p1, p2 = 0, 0
            while p1<len(start) and p2<len(end):
                while p1<len(start) and start[p1]=="X":
                    p1+=1
                while p2<len(end) and end[p2]=="X":
                    p2+=1
                if p1==len(start) and p2==len(end):
                    return True
                if p1==len(start) or p2==len(end):
                    return False
                if start[p1]!=end[p2]:
                    return False
                if start[p1]=="L" and p1<p2:
                    return False
                if start[p1]=="R" and p1>p2:
                    return False
                p1+=1
                p2+=1
            return True