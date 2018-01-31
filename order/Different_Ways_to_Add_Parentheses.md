# 241. Different Ways to Add Parentheses

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1

    Input: "2-1-1".
    
    ((2-1)-1) = 0
    (2-(1-1)) = 2
    Output: [0, 2]


Example 2

    Input: "2*3-4*5"
    
    (2*(3-(4*5))) = -34
    ((2*3)-(4*5)) = -14
    ((2*(3-4))*5) = -10
    (2*((3-4)*5)) = -10
    (((2*3)-4)*5) = 10
    Output: [-34, -14, -10, -10, 10]
    
## Method:

divide and conquer, list slicing:

    class Solution(object):
        def diffWaysToCompute(self, input):
            """
            :type input: str
            :rtype: List[int]
            """
            opt={'-':lambda x, y: x-y, '+':lambda x, y: x+y, '*':lambda x, y: x*y}
            res=[]
            for i in range(len(input)):
                if input[i] in opt:
                    for x in self.diffWaysToCompute(input[:i]):
                        for y in self.diffWaysToCompute(input[i+1:]):
                            res.append(opt[input[i]](x, y))
            return res if res else [int(input)] 
            
same idea, index:

    class Solution(object):
        def diffWaysToCompute(self, input):
            """
            :type input: str
            :rtype: List[int]
            """
            opt={'-':lambda x, y: x-y, '+':lambda x, y: x+y, '*':lambda x, y: x*y}
            
            def helper(lo, hi):
                ans=[]
                for i in range(lo, hi+1):
                    if input[i] in opt:
                        for x in helper(lo, i-1):
                            for y in helper(i+1, hi):
                                ans.append(opt[input[i]](x, y))
                return ans if ans else [int(input[lo:hi+1])]
            
            return helper(0, len(input)-1)
            
using dict, faster:

    class Solution(object):
        def diffWaysToCompute(self, input):
            """
            :type input: str
            :rtype: List[int]
            """
            opt={'-':lambda x, y: x-y, '+':lambda x, y: x+y, '*':lambda x, y: x*y}
            d={}
            
            def helper(lo, hi):
                if (lo, hi) in d:
                    return d[(lo, hi)]
                ans=[]
                for i in range(lo, hi+1):
                    if input[i] in opt:
                        for x in helper(lo, i-1):
                            for y in helper(i+1, hi):
                                ans.append(opt[input[i]](x, y))
                d[(lo, hi)]= ans if ans else [int(input[lo:hi+1])]
                return d[(lo, hi)]
            
            return helper(0, len(input)-1)