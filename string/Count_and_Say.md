# 038. Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:

    1. 1
    2. 11
    3. 21
    4. 1211
    5. 111221

- 1 is read off as "one 1" or 11.
- 11 is read off as "two 1s" or 21.
- 21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

    Input: 1
    Output: "1"

Example 2:

    Input: 4
    Output: "1211"
    
## Method:

    class Solution(object):
        def countAndSay(self, n):
            """
            :type n: int
            :rtype: str
            """
            res='1'
            for i in range(n-1):
                tmp, v, count='', res[0], 0
                for s in res:
                    if s==v:
                        count+=1
                    else:
                        tmp+=str(count)+v
                        v=s
                        count=1
                tmp+=str(count)+v
                res=tmp
            return res
            