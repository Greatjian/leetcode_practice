# 17. Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

see dict in method

    Input:Digit string "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

## Method:

    class Solution(object):
        def letterCombinations(self, digits):
            """
            :type digits: str
            :rtype: List[str]
            """
            if not len(digits):
                return []
            res=[]
            hashmap={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
            self.dfs(digits,hashmap,'',res)
            return res
            
            
        def dfs(self, digits, hashmap, path, res):
            if not digits:
                res.append(path)
                return
            for i in hashmap[digits[0]]:
                # path+=i 这样每个答案都要走完所有path，不行
                self.dfs(digits[1:],hashmap,path+i,res)
                # return 只会显示一个答案，不行
            