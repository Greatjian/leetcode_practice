# 227. Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:

- "3+2*2" = 7
- " 3/2 " = 1
- " 3+5 / 2 " = 5

Note: Do not use the eval built-in library function.

## Method:

    class Solution(object):
        def calculate(self, s):
            """
            :type s: str
            :rtype: int
            """
            stack=[]
            sign='+'
            num=0
            s+='+'
            for i in range(len(s)):
                if s[i].isdigit():
                    num=num*10+int(s[i])
                else:
                    if s[i].isspace():
                        continue
                    if sign=='+':
                        stack.append(num)
                    if sign=='-':
                        stack.append(-num)
                    if sign=='*':
                        stack.append(stack.pop()*num)
                    if sign=='/':
                        temp=stack.pop()
                        if temp>=0 or temp%num==0:
                            stack.append(temp/num)
                        else:
                            stack.append(temp/num+1)
                    sign=s[i]
                    num=0
            return sum(stack)