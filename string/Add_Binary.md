# 067. Add Binary


Given two binary strings, return their sum (also a binary string).

For example,

    a = "11"
    b = "1"
    Return "100".
    
## Method:

补位+carry on

    class Solution(object):
        def addBinary(self, a, b):
            """
            :type a: str
            :type b: str
            :rtype: str
            """
            if len(a)>len(b):
                b='0'*(len(a)-len(b))+b
            else:
                a='0'*(len(b)-len(a))+a
            carry=0
            c=[]
            for i in range(len(a)-1, -1, -1):
                c.append(int(a[i])+int(b[i])+carry)
                carry=c[-1]/2
                c[-1]=str(c[-1]%2)
            if carry:
                c.append('1')
            return ''.join(c[::-1])