# 784. Letter Case Permutation

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:

    Input: S = "a1b2"
    Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
    
    Input: S = "3z4"
    Output: ["3z4", "3Z4"]
    
    Input: S = "12345"
    Output: ["12345"]

Note:

- S will be a string with length at most 12.
- S will consist only of letters or digits.

## Method:

backtracking:

    class Solution(object):
        def letterCasePermutation(self, S):
            """
            :type S: str
            :rtype: List[str]
            """
            res=[]
            self.helper(S, '', res)
            return res
            
        def helper(self, s, path, res):
            if not s:
                res.append(path)
                return
            if s[0].isdigit():
                self.helper(s[1:], path+s[0], res)
            else:
                self.helper(s[1:], path+s[0].lower(), res)
                self.helper(s[1:], path+s[0].upper(), res)
                
change from slicing to index:

    class Solution(object):
        def letterCasePermutation(self, S):
            """
            :type S: str
            :rtype: List[str]
            """
            
            def helper(idx, path, res):
                if idx==len(S):
                    res.append(path)
                    return
                if S[idx].isdigit():
                    helper(idx+1, path+S[idx], res)
                else:
                    helper(idx+1, path+S[idx].lower(), res)
                    helper(idx+1, path+S[idx].upper(), res)
                    
            res=[]
            helper(0, '', res)
            return res