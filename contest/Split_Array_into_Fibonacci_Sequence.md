# 842. Split Array into Fibonacci Sequence

Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

    Input: "123456579"
    Output: [123,456,579]

Example 2:

    Input: "11235813"
    Output: [1,1,2,3,5,8,13]

Example 3:

    Input: "112358130"
    Output: []
    Explanation: The task is impossible.

Example 4:

    Input: "0123"
    Output: []
    Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.

Example 5:

    Input: "1101111"
    Output: [110, 1, 111]
    Explanation: The output [11, 0, 11, 11] would also be accepted.

Note:

- 1 <= S.length <= 200
- S contains only digits.

## Method:

    class Solution(object):
        def splitIntoFibonacci(self, S):
            """
            :type S: str
            :rtype: List[int]
            """
            res=[]
            for i in range(len(S)/2+2):
                for j in range(i+1, len(S)):
                    a=int(S[:i+1])
                    b=int(S[i+1:j+1])
                    s=S[j+1:]
                    if S[0]=='0' and i>=1 or S[i+1]=='0' and j-i>=2 or a>2147483647 or b>2147483647:
                        continue
                    self.helper(a, b, s, [a, b], res)
                    if res:
                        return res[0]
            return []
                    
        def helper(self, a, b, s, path, res):
            if not s:
                if len(path)>2:
                    res.append(path)
                return
            for i in range(len(s)):
                num=int(s[:i+1])
                if s[0]=='0' and i>=1 or num>2147483647:
                    continue
                if num==a+b:
                    self.helper(b, num, s[i+1:], path+[num], res)
                    
## Solution:

iterative, faster (866->42):

    class Solution(object):
        def splitIntoFibonacci(self, S):
            """
            :type S: str
            :rtype: List[int]
            """
            for i in range(len(S)/2+2):
                a=int(S[:i+1])
                if S[0]=='0' and i>=1 or a>2**31-1:
                    break
                for j in range(i+1, len(S)-1):
                    b=int(S[i+1:j+1])
                    if S[i+1]=='0' and j-i>=2 or b>2**31-1:
                        break
                    fib=[a, b]
                    k=j+1
                    pre, cur=a,b
                    while k<len(S):
                        if S[k:k+len(str(pre+cur))]==str(pre+cur) and pre+cur<2**31-1:
                            k+=len(str(pre+cur))
                            fib.append(pre+cur)
                            pre, cur=cur, pre+cur
                        else:
                            break
                    if k==len(S) and len(fib)>2:
                        return fib
            return []