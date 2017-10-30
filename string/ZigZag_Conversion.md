# 6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

"abcdefghijk", 5 --> 

a  i
b  h  j
c  g  k
d  f
e

-->

"aibhjcgkdfe'


## Method:

''.join()

    class Solution(object):
        def convert(self, s, numRows):
            """
            :type s: str
            :type numRows: int
            :rtype: str
            """
            if numRows<=1:
                return s
            res=['']*numRows
            i, step=0, 1
            for c in s:
                res[i]+=c
                if i==0:
                    step=1
                elif i==numRows-1:
                    step=-1
                i+=step
            return ''.join(res)
