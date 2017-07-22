# 066. Plus One

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

## Method:
从列表最后递归遍历，分别判断是否为9以及9是否在最高位：

    class Solution(object):
        def plusOne(self, digits):
            """
            :type digits: List[int]
            :rtype: List[int]
            """
            return self.plus(digits,-1)

        def plus(self,digits,start):
            if digits[start]!=9:
                digits[start]+=1
                return digits
            else:
                digits[start]=0
                if start==-len(digits):
                    digits.insert(0,1)
                    return digits
                else:
                    start-=1
                    self.plus(digits,start)
                    return digits   #递归值返回的对象是上一层的递归函数而非总调用函数，故需要return

## Solution:
遍历亦可使用for loop，依旧分情况考虑，每一位是否含9以及进位的情况:

判断9是否在最高位使用carry参数，很精彩。

    class Solution(object):
        def plusOne(self, digits):
            """
            :type digits: List[int]
            :rtype: List[int]
            """
            carryon = 1
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] != 9:
                    digits[i] += 1
                    carryon=0
                    break
                else:
                    digits[i] = 0
            if carryon==1:
                digits.insert(0,1)
            return digits