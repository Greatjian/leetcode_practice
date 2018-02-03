# 254. Factor Combinations

Numbers can be regarded as product of its factors. For example,

    8 = 2 x 2 x 2;
      = 2 x 4.

Write a function that takes an integer n and return all possible combinations of its factors.

Note: 
- You may assume that n is always positive.
- Factors should be greater than 1 and less than n.

Examples: 

    input: 1
    output: 
    []

    input: 37
    output: 
    []

    input: 12
    output:
    [
      [2, 6],
      [2, 2, 3],
      [3, 4]
    ]

    input: 32
    output:
    [
      [2, 16],
      [2, 2, 8],
      [2, 2, 2, 4],
      [2, 2, 2, 2, 2],
      [2, 4, 4],
      [4, 8]
    ]
    
## Method:

idx, prevent (2,3,2...):

    class Solution(object):
        def getFactors(self, n):
            """
            :type n: int
            :rtype: List[List[int]]
            """
            res=[]
            self.helper(2, n, [], res)
            return res
            
        def helper(self, idx, n, path, res):
            for i in range(idx, int(n**0.5+1)):
                if n%i==0:
                    res.append(path+[i, n/i])
                    self.helper(i, n/i, path+[i], res)
            