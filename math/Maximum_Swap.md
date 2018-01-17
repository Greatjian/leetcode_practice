# 670. Maximum Swap

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:

    Input: 2736
    Output: 7236
    Explanation: Swap the number 2 and the number 7.

Example 2:

    Input: 9973
    Output: 9973
    Explanation: No swap.

Note:
- The given number is in the range [0, 108]

## Method:

dfs, find position to swap:

    class Solution(object):
        def maximumSwap(self, num):
            """
            :type num: int
            :rtype: int
            """
            l=list(map(int, str(num)))
            l=self.helper(l)
            res=0
            for i in range(len(l)):
                res=res*10+l[i]
            return res
            
        def helper(self, num):
            if not num:
                return []
            if num[0]==max(num):
                return [num[0]]+self.helper(num[1:])
            idx=len(num)-1-num[::-1].index(max(num))
            num[0], num[idx]=num[idx], num[0]
            return num
            
iteration:

    class Solution(object):
        def maximumSwap(self, num):
            """
            :type num: int
            :rtype: int
            """
            l=list(map(int, str(num)))
            for i in range(len(l)):
                if l[i]==max(l[i:]):
                    continue
                idx=i+len(l[i:])-1-l[i:][::-1].index(max(l[i:]))
                l[i], l[idx]=l[idx], l[i]
                break
            res=0
            for i in range(len(l)):
                res=res*10+l[i]
            return res
            
## Solution:

same idea, two for-loops:

    class Solution(object):
        def maximumSwap(self, num):
            """
            :type num: int
            :rtype: int
            """
            l=list(map(int, str(num)))
            for i in range(len(l)):
                m=l[i]
                for j in range(i+1, len(l)):
                    if l[j]>=m:
                        m=l[j]
                        idx=j
                if l[i]!=m:
                    l[i], l[idx]=l[idx], l[i]
                    break
            return int(''.join(map(str, l)))
            
bucket sort, more quickly:

    class Solution(object):
        def maximumSwap(self, num):
            """
            :type num: int
            :rtype: int
            """
            l=list(map(int, str(num)))
            d={val:idx for idx, val in enumerate(l)}
            for i in range(len(l)):
                for j in range(9, l[i], -1):
                    if d.get(j)>i:
                        l[i], l[d[j]]=l[d[j]], l[i]
                        return int(''.join(map(str, l)))
            return int(''.join(map(str, l)))