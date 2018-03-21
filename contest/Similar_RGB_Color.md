# 800. Similar RGB Color

In the following, every capital letter represents some hexadecimal digit from 0 to f.

The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.  For example, "#15c" is shorthand for the color "#1155cc".

    Now, say the similarity between two colors "#ABCDEF" and "#UVWXYZ" is -(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2.

Given the color "#ABCDEF", return a 7 character color that is most similar to #ABCDEF, and has a shorthand (that is, it can be represented as some "#XYZ"

Example 1:

    Input: color = "#09f166"
    Output: "#11ee66"

Explanation:  

    The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
    This is the highest among any shorthand color.

Note:

- color is a string of length 7.
- color is a valid RGB color: for i > 0, color[i] is a hexadecimal digit from 0 to f
- Any answer which has the same (highest) similarity as the best answer will be accepted.
- All inputs and outputs should use lowercase letters, and the output is 7 characters.

## Method:

brute force:

    class Solution(object):
        def similarRGB(self, color):
            """
            :type color: str
            :rtype: str
            """
            res='#'
            for i in range(1, len(color), 2):
                ans, cnt='', float('inf')
                for j in ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff']:
                    if cnt>abs(int(color[i:i+2], 16)-int(j, 16)):
                        ans=j
                        cnt=abs(int(color[i:i+2], 16)-int(j, 16))
                res+=ans
            return res
            
每次位置最多比较三个数：

    class Solution(object):
        def similarRGB(self, color):
            """
            :type color: str
            :rtype: str
            """
            s='0123456789abcdef'
            d={s[i]:i for i in range(len(s))}
            res='#'
            for i in range(1, len(color), 2):
                ans, cnt='', float('inf')
                element=[color[i]*2]
                if color[i]!='0':
                    element.append(s[d[color[i]]-1]*2)
                if color[i]!='f':
                    element.append(s[d[color[i]]+1]*2)
                for j in element:
                    if cnt>abs(int(color[i:i+2], 16)-int(j, 16)):
                        ans=j
                        cnt=abs(int(color[i:i+2], 16)-int(j, 16))
                res+=ans
            return res