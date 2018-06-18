# 402. Remove K Digits

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
- The length of num is less than 10002 and will be ≥ k.
- The given num does not contain any leading zero.

Example 1:

    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:

    Input: num = "10200", k = 1
    Output: "200"
    Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:

    Input: num = "10", k = 2
    Output: "0"
    Explanation: Remove all the digits from the number and it is left with nothing which is 0.

## Method:

compare and append, O(n^2), 1006ms:

    class Solution(object):
        def removeKdigits(self, num, k):
            """
            :type num: str
            :type k: int
            :rtype: str
            """
            l, kk=len(num), k
            if k==l:
                return '0'
            num=map(int, list(num))
            stack=[]
            while len(stack)<l-kk:
                minIdx, minVal=-1, float('inf')
                for i in range(min(k+1, len(num))):
                    if num[i]<minVal:
                        minVal=num[i]
                        minIdx=i
                k-=minIdx
                stack.append(num[minIdx])
                num=num[minIdx+1:]
            res=0
            for n in stack:
                res=res*10+n
            return str(res)
                            
same idea, change list slicing to index, O(nk), 377ms:

    class Solution(object):
        def removeKdigits(self, num, k):
            """
            :type num: str
            :type k: int
            :rtype: str
            """
            l, kk=len(num), k
            if k==l:
                return '0'
            num=map(int, list(num))
            stack=[]
            start=0
            while len(stack)<l-kk:
                minIdx, minVal=-1, float('inf')
                for i in range(start, start+min(k+1, len(num))):
                    if num[i]<minVal:
                        minVal=num[i]
                        minIdx=i
                k-=minIdx-start
                stack.append(num[minIdx])
                start=minIdx+1
            res=0
            for n in stack:
                res=res*10+n
            return str(res)

## Solution:

one pass stack, O(n), 128ms:

    class Solution(object):
        def removeKdigits(self, num, k):
            """
            :type num: str
            :type k: int
            :rtype: str
            """
            if k==len(num):
                return '0'
            num=map(int, list(num))
            stack=[]
            for n in num:
                if not stack or stack[-1]<=n:
                    stack.append(n)
                else:
                    while stack and stack[-1]>n and k>0:
                        stack.pop()
                        k-=1
                    stack.append(n)
            while k:
                stack.pop()
                k-=1
            res=0
            for n in stack:
                res=res*10+n
            return str(res)
                                            