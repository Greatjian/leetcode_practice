# 423. Reconstruct Original Digits from English

Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
- Input contains only lowercase English letters.
- Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
- Input length is less than 50,000.

Example 1:

    Input: "owoztneoer"
    
    Output: "012"

Example 2:

    Input: "fviefuro"
    
    Output: "45"
    
## Method:

寻找特殊字符：

    class Solution(object):
        def originalDigits(self, s):
            """
            :type s: str
            :rtype: str
            """
            res=[0]*10
            d=collections.Counter(s)
            res[0], res[2], res[6], res[8], res[4]=d['z'], d['w'], d['x'], d['g'], d['u']
            res[7]=d['s']-res[6]
            res[5]=d['f']-res[4]
            res[3]=d['h']-res[8]
            res[9]=d['i']-res[8]-res[5]-res[6]
            res[1]=d['o']-res[0]-res[2]-res[4]
            ans=''
            for i in range(len(res)):
                ans+=str(i)*res[i]
            return ans