# 856. Score of Parentheses

Given a balanced parentheses string S, compute the score of the string based on the following rule:

- () has score 1
- AB has score A + B, where A and B are balanced parentheses strings.
- (A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

    Input: "()"
    Output: 1

Example 2:

    Input: "(())"
    Output: 2

Example 3:

    Input: "()()"
    Output: 2

Example 4:

    Input: "(()(()))"
    Output: 6
 

Note:

- S is a balanced parentheses string, containing only ( and ).
- 2 <= S.length <= 50

## Method:

    class Solution(object):
        def scoreOfParentheses(self, S):
            """
            :type S: str
            :rtype: int
            """
            res=0
            stack=[]
            for i in S:
                if i=='(':
                    stack.append(i)
                elif stack[-1]=='(':
                    stack.pop()
                    stack.append(1)
                else:
                    tmp=0
                    while stack[-1]!='(':
                        tmp+=stack.pop()
                    stack.pop()
                    stack.append(tmp*2)
            return sum(stack)