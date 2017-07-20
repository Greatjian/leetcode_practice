# 040. Combination Sum II

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 

    [
      [1, 7],
      [1, 2, 5],
      [2, 6],
      [1, 1, 6]
    ]
   
## Method:
类似前题，采用dfs，但第一次尝试后面需要删除列表中重复元素，O(n^2)超时。

    class Solution(object):
        def combinationSum2(self, candidates, target):
            """
            :type candidates: List[int]
            :type target: int
            :rtype: List[List[int]]
            """
            candidates.sort()
            res=[]
            self.solsum(candidates, target,[],res,0)
            result=[]
            for i in res:
                if i not in result:
                    result.append(i)
            return result
            
        def solsum(self, candidates, target, ans, res, start):
            if sum(ans)==target:
                res.append(ans)
            elif sum(ans)>target:
                return
            else:
                for i in range(start,len(candidates)):
                    self.solsum(candidates, target, ans+[candidates[i]], res, i+1)
            
            
## Solution
删除重复元素可在dfs中完成：

删除采用while循环

```
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res=[]
        self.solsum(candidates, target,[],res, 0)
        return res
        
    def solsum(self, candidates, target, ans, res, start):
        i= start
        if target==0:
            res.append(ans)
        else:
            while i < len(candidates):
                if target<candidates[i]:
                    return
                self.solsum(candidates, target-candidates[i], ans+[candidates[i]], res, i+1)
                while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                    i+=1
                i+=1
                
        
```
for-range则不行

    def solsum(self, candidates, target, ans, res, start):
        if target==0:
            res.append(ans)
        else:
            for i in range(start, len(candidates)):
                if target<candidates[i]:
                    return
                self.solsum(candidates, target-candidates[i], ans+[candidates[i]], res, i+1)
                while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                    i+=1