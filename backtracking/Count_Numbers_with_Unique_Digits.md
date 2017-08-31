# 357. Count Numbers with Unique Digits

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])

## Method:
dfs太复杂

    class Solution(object):
        def countNumbersWithUniqueDigits(self, n):
            """
            :type n: int
            :rtype: int
            """
            nums=[i for i in range(10)]
            count=[]
            flag=0
            self.isUniqueDigits(nums,n,count,flag)
            return len(count)
            
        def isUniqueDigits(self,nums,n,count,flag):
            if n==0:
                count.append(1)
                return
            for i in range(len(nums)):
                if nums[i]==0 and flag==0:
                    self.isUniqueDigits(nums,n-1,count,flag)
                else:
                    self.isUniqueDigits(nums[:i]+nums[i+1:],n-1,count,1)
## Solution:
math:

>0:1
>
>1:9
>
>2:9* 9
>
>3:9* 9* 8
>
>...

    class Solution(object):
        def countNumbersWithUniqueDigits(self, n):
            """
            :type n: int
            :rtype: int
            """
            if n==0:
                return 1
            flag=True
            sum=0
            avail=9
            mult=1
            for i in range(n):
                if i==0:
                    sum+=10
                elif flag:
                    mult=9*avail
                    sum+=mult
                    avail-=1
                    flag=False
                else:
                    mult*=avail
                    avail-=1
                    sum+=mult
            return sum

dp:递推

    class Solution(object):
        def countNumbersWithUniqueDigits(self, n):
            """
            :type n: int
            :rtype: int
            """
            if n==0:
                return 1
            if n==1:
                return 10
            dp=[1]*(n+1)
            dp[1]=9
            temp=9
            for i in range(2,n+1):
                dp[i]=dp[i-1]*temp
                temp-=1
            return sum(dp)