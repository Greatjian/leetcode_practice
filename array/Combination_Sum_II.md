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
删除重复元素可在dfs中完成，
注意删除横向元素而非纵向:
>([1,1,2,3...]中删除重复的[1,2,3...]，不删除[1,1,2...])

删除采用while循环：

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
for-range则不行(for loop中i顺序增加，后面i+=1改变赋值没有效果)


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

可更改判断条件实现


    def solsum(self, candidates, target, ans, res, start):
        if target==0:
            res.append(ans)
        else:
            for i in range(start,len(candidates)):
                if target<candidates[i]:
                    return
                if i!=start and i+1<len(candidates) and candidates[i]==candidates[i-1]:
                    continue
                self.solsum(candidates, target-candidates[i], ans+[candidates[i]], res, i+1)

最佳：

    class Solution(object):
        def combinationSum2(self, candidates, target):
            """
            :type candidates: List[int]
            :type target: int
            :rtype: List[List[int]]
            """
            candidates.sort()
            res=[]
            self.solsum(candidates, target,[],res)
            return res
            
        def solsum(self, candidates, target, ans, res):
            if target==0:
                res.append(ans)
            for i in range(len(candidates)):
                if target>=candidates[i]:
                    if i-1>=0 and candidates[i]==candidates[i-1]:
                        continue
                    self.solsum(candidates[i+1:], target-candidates[i], ans+[candidates[i]], res)