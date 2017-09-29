# 647. Palindromic Substrings

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

    Input: "abc"
    Output: 3
    
    Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

    Input: "aaa"
    Output: 6
    
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:
- The input string length won't exceed 1000.

## Method:
对称中心法：

    class Solution(object):
        def countSubstrings(self, s):
            """
            :type s: str
            :rtype: int
            """
            l=len(s)
            ans=0
            for i in range(2*l-1):
                left=i/2
                right=left+i%2
                while left>=0 and right<l and s[left]==s[right]:
                    ans+=1
                    left-=1
                    right+=1
            return ans
            
## Solution:

    class Solution(object):
        def countSubstrings(self, s):
            """
            :type s: str
            :rtype: int
            """
            size = len(s)
            queue = collections.deque((x, x) for x in range(size))
            for x in range(size - 1):
                if s[x] == s[x + 1]:
                    queue.append((x, x + 1))
            ans = 0
            while queue:
                x, y = queue.popleft()
                ans += 1
                if x - 1 >= 0 and y + 1 < size and s[x - 1] == s[y + 1]:
                    queue.append((x - 1, y + 1))
            return ans