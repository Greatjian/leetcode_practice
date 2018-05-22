# 838. Push Dominoes

There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.



After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state. 

Example 1:

    Input: ".L.R...LR..L.."
    Output: "LL.RR.LLRRLL.."

Example 2:

    Input: "RR.L"
    Output: "RR.L"

Explanation: The first domino expends no additional force on the second domino.

Note:

- 0 <= N <= 10^5
- String dominoes contains only 'L', 'R' and '.'

## Method:

    class Solution(object):
        def pushDominoes(self, dominoes):
            """
            :type dominoes: str
            :rtype: str
            """
            dp=[['.', float('inf')]]*len(dominoes)
            for i in range(len(dominoes)):
                if dominoes[i]=='R':
                    dp[i]=['R', 0]
                elif dominoes[i]=='L':
                    dp[i]=['L', 0]
            for i in range(1, len(dp)):
                if dp[i-1][0]=='R' and dp[i][0]=='.':
                    dp[i]=['R', dp[i-1][1]+1]
            for i in range(len(dp)-2, -1, -1):
                if dp[i+1][0]=='L' and dp[i][1]>dp[i+1][1]+1:
                    dp[i]=['L', dp[i+1][1]+1]
                elif dp[i+1][0]=='L' and dp[i][1]==dp[i+1][1]+1:
                    dp[i]=['.', dp[i+1][1]+1]
            return ''.join(i[0] for i in dp)

modified: three passes, using cnt:

    class Solution(object):
        def pushDominoes(self, dominoes):
            """
            :type dominoes: str
            :rtype: str
            """
            l=len(dominoes)
            d=list(dominoes)
            cnt=[float('inf')]*l
            for i in range(l):
                if d[i]!='.':
                    cnt[i]=0
            for i in range(1, l):
                if d[i-1]=='R' and d[i]=='.':
                    d[i]='R'
                    cnt[i]=cnt[i-1]+1
            for i in range(len(cnt)-2, -1, -1):
                if d[i+1]=='L' and cnt[i]>cnt[i+1]+1:
                    d[i]='L'
                    cnt[i]=cnt[i+1]+1
                elif d[i+1]=='L' and cnt[i]==cnt[i+1]+1:
                    d[i]='.'
                    cnt[i]=cnt[1]+1
            return ''.join(d)