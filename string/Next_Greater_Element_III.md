# 556. Next Greater Element III

Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

    Input: 12
    Output: 21

Example 2:

    Input: 21
    Output: -1
    
## Method:

找到两个index交换位置，后部分sort:

    class Solution(object):
        def nextGreaterElement(self, n):
            """
            :type n: int
            :rtype: int
            """
            s=map(int, str(n))
            a=None
            for i in range(len(s)-2, -1, -1):
                if s[i]<s[i+1]:
                    a=i
                    break
            if a is None:
                return -1
            m=max(s[i+1:])
            b=i+1+s[i+1:].index(m)
            for i in range(i+1, len(s)):
                if s[i]>s[a] and s[i]<m:
                    m=s[i]
                    b=i
            s[a], s[b]=s[b], s[a]
            s[a+1:]=sorted(s[a+1:])
            res=int(''.join(map(str, s)))
            return res if res<=2147483647 else -1
            