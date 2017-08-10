# 022. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

    [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]
    
## Method:

    class Solution(object):
        def generateParenthesis(self, n):
            """
            :type n: int
            :rtype: List[str]
            """
            res=[]
            self.getParenthesis(n, n, "", res)
            return res
            
        def getParenthesis(self, left, right, path, res):
            if left==0 and right==0:
                res.append(path)
                return
            if left>0:
                self.getParenthesis(left-1, right, path+"(", res)
            if left<right:
                self.getParenthesis(left, right-1, path+")", res)