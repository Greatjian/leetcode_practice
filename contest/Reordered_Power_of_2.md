## 869. Reordered Power of 2

Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.

Example 1:

    Input: 1
    Output: true

Example 2:

    Input: 10
    Output: false

Example 3:

    Input: 16
    Output: true

Example 4:

    Input: 24
    Output: false

Example 5:

    Input: 46
    Output: true
    
## Method:

using using backtracking and memorization for permutation, 1784 ms.

no memo will lead to TLE, time complexity is O(N!):

    class Solution(object):
        def reorderedPowerOf2(self, N):
            """
            :type N: int
            :rtype: bool
            """
            def isPower(N):
                s=bin(N)[2:]
                return s[0]=='1' and '1' not in s[1:]
                # if N<1:
                #     return False
                # while N>1:
                #     if N%2==1:
                #         return False
                #     N/=2
                # return N==1
            
            def helper(l, path, d):
                if not l:
                    # print path
                    if isPower(path):
                        return True
                    return False
                if path in d:
                    return False
                for i in range(len(l)):
                    if not path and l[i]==0:
                        continue
                    if helper(l[:i]+l[i+1:], path*10+l[i], d):
                        return True
                d[path]=False
                return False
            
            l=map(int, str(N))
            d={}
            return helper(l, 0, d)
            
## Solution:

string can also compared using counter(O(N)) or sorting(O(NlogN)).

total complexity is O(log^2 N), 28ms:

    class Solution(object):
        def reorderedPowerOf2(self, N):
            """
            :type N: int
            :rtype: bool
            """
            s=str(N)
            num=1
            while len(str(num))<len(s):
                num*=2
            while len(str(num))==len(s):
                if collections.Counter(str(num))==collections.Counter(s):
                    return True
                num*=2
            return False