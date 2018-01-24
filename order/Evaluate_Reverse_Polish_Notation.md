# 150. Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  
      ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
      ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

## Method:

    class Solution(object):
        def evalRPN(self, tokens):
            """
            :type tokens: List[str]
            :rtype: int
            """
            stack=[]
            for token in tokens:
                if token not in ['+', '-', '*', '/']:
                    stack.append(token)
                else:
                    t1=int(stack.pop())
                    t2=int(stack.pop())
                    if token=='+':
                        val=str(t2+t1)
                    elif token=='-':
                        val=str(t2-t1)
                    elif token=='*':
                        val=str(t2*t1)
                    else:
                        if t2/t1<0 and t2%t1:
                            val=str(t2/t1+1)
                        else:
                            val=str(t2/t1)
                    stack.append(val)
            return int(stack[0])
            
## Solution:

So elegent:

    class Solution(object):
        def evalRPN(self, tokens):
            """
            :type tokens: List[str]
            :rtype: int
            """
            stack = []
            ops = {'+':lambda x, y: x+y, '-':lambda x, y: x-y, '*':lambda x, y: x*y, 
                   '/':lambda x, y: abs(x)/abs(y) * (1 if x * y >= 0 else -1)}
            for t in tokens:
                if t in ops:
                    op = ops[t]
                    v2 = stack.pop()
                    v1 = stack.pop()
                    stack.append(op(v1, v2))
                else:
                    stack.append(int(t))
            return stack[-1]