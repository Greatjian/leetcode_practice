# 071. Simplify Path

Given an absolute path for a file (Unix-style), simplify it.

For example,

    path = "/home/", => "/home"
    path = "/a/./b/../../c/", => "/c"

Corner Cases:
- Did you consider the case where path = "/../"?
- In this case, you should return "/".
- Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
- In this case, you should ignore redundant slashes and return "/home/foo".

## Method:

split and join:

    class Solution(object):
        def simplifyPath(self, path):
            """
            :type path: str
            :rtype: str
            """
            p=path.split('/')
            ans=[]
            for i in range(len(p)):
                if not p[i]:
                    continue
                if p[i]=='.':
                    continue
                if p[i]=='..':
                    ans=ans[:-1]
                    continue
                ans.append(p[i])
            if len(ans)>1 and ans[-1]=='/':
                ans=ans[:-1]
            return '/'+'/'.join(ans)
            
## Solution:

pop简写：

    class Solution(object):
        def simplifyPath(self, path):
            """
            :type path: str
            :rtype: str
            """
            p=path.split('/')
            ans=[]
            for i in range(len(p)):
                if not p[i]:
                    continue
                if p[i]=='.':
                    continue
                if p[i]=='..':
                    ans.pop() if ans else None
                    continue
                ans.append(p[i])
            return '/'+'/'.join(ans)