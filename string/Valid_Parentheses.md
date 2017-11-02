# 020. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

## Method:

    class Solution(object):
        def isValid(self, s):
            """
            :type s: str
            :rtype: bool
            """
            stack=[]
            for i in s:
                if i=='(' or i=='[' or i=='{':
                    stack.append(i)
                else:
                    if not stack:
                        return False
                    o=stack.pop()
                    if (i==')' and o!='(') or (i=='}' and o!='{') or (i==']' and o!='['):
                        return False
            return stack==[]