# 039. Combination Sum

Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 

    [
      [7],
      [2, 2, 3]
    ]
    
## Method:
使用回溯法（深度优先搜索），可正推亦可倒推。

```
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res=[]
        self.solsum (candidates, 0, target, [], res)
        return res
        
    def solsum(self, candidates, start, target, ans, res):
        if target==0:
            return res.append(ans)
        for i in range(start, len(candidates)):
            if candidates[i]>target:
                return
            self.solsum(candidates, i, target-candidates[i], ans+[candidates[i]], res)
        
```

```
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res=[]
        self.solsum (candidates, target, [], res)
        return res
        
    def solsum(self, candidates, target, ans, res):
        if target==sum(ans):
            return res.append(ans)
        elif target<sum(ans):
            return
        else:
            for i in range(len(candidates)):
                self.solsum(candidates[i:], target, ans+[candidates[i]], res)
```