# 093. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

## Method:
valid IP address: 四段数字，每段1-3位，大小在0-255间，若非0则首位不能有0：

    class Solution(object):
        def restoreIpAddresses(self, s):
            """
            :type s: str
            :rtype: List[str]
            """
            res=[]
            self.dfs(s,'',res,4)
            return res
        
        def dfs(self,s,path,res,n):
            if n==0 and not s:
                res.append(path)
            if path:
                path+='.'
            if n*3>=len(s) and n>0:
                for i in range(3):
                    if len(s[0:i+1])>1 and s[0]=='0':
                        continue
                    if len(s)>i and int(s[0:i+1])<=255:
                        self.dfs(s[i+1:],path+s[0:i+1],res,n-1)