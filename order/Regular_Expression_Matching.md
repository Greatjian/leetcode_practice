# 010. Regular Expression Matching

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:

    isMatch("aa","a") → false
    isMatch("aa","aa") → true
    isMatch("aaa","aa") → false
    isMatch("aa", "a*") → true
    isMatch("aa", ".*") → true
    isMatch("ab", ".*") → true
    isMatch("aab", "c*a*b") → true

## Method:

dp，注意base case and 0/1 index:

    class Solution(object):
        def isMatch(self, s, p):
            """
            :type s: str
            :type p: str
            :rtype: bool
            """
            m, n=len(s), len(p)
            dp=[[False]*(n+1) for _ in range(m+1)]
            for j in range(n+1):
                if j==0:
                    dp[0][j]=True
                    continue
                if j-1>=0 and dp[0][j-2] and p[j-1]=="*":
                    dp[0][j]=True
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if p[j-1]==s[i-1] or p[j-1]==".":
                        dp[i][j]=dp[i-1][j-1]
                    elif p[j-1]=="*":
                        if j-2>=0 and p[j-2]!=s[i-1] and p[j-2]!=".":
                            dp[i][j]=dp[i][j-2]
                        else:
                            dp[i][j]=dp[i-1][j] or dp[i-1][j-1] or dp[i][j-2]
            return dp[-1][-1]