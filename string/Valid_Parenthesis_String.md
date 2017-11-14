# 678. Valid Parenthesis String

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
- An empty string is also valid.

Example 1:

    Input: "()"
    Output: True

Example 2:

    Input: "(*)"
    Output: True

Example 3:

    Input: "(*))"
    Output: True

Note:
- The string size will be in the range [1, 100].

## Method:

first try using stack, but the position of "*" matters, wrong:

    class Solution(object):
        def checkValidString(self, s):
            """
            :type s: str
            :rtype: bool
            """
            stack=[]
            count=0
            for i in s:
                if i=='(':
                    stack.append('(')
                if i=='*':
                    count+=1
                if i==')':
                    if not stack:
                        count-=1
                        if count<0:
                            return False
                    else:
                        stack.pop()
            return len(stack)<=count and count>=0

adding more requirement, pass:

    class Solution(object):
        def checkValidString(self, s):
            """
            :type s: str
            :rtype: bool
            """
            stack=[]
            count=0
            for i in s:
                if i=='(':
                    stack.append('(')
                if i=='*':
                    stack.append('*')
                if i==')':
                    if not stack:
                        return False
                    while stack and stack.pop()!='(':
                            count+=1
                            if not stack:
                                if count==0:
                                    return False
                                count-=1
                    stack+=['*']*count
                    count=0
            for i in range(len(stack)-1, -1, -1):
                if stack[i]=='*':
                    count+=1
                else:
                    count-=1
                if count<0:
                    return False
            return True
            
## Solution:

lo for ( and *, hi for )

    class Solution(object):
        def checkValidString(self, s):
            """
            :type s: str
            :rtype: bool
            """
            lo = 0
            hi = 0
            for i in range(len(s)):
                if s[i] == ')':
                    lo = max(0, lo-1)
                    hi -= 1
                elif s[i] == '(':
                    lo += 1
                    hi += 1
                else:
                    lo = max(0, lo-1)
                    hi += 1
                if hi < 0:
                    return False
            return lo == 0
                