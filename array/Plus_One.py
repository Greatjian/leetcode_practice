class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        print(self.plus(digits,-1))
        return (self.plus(digits,-1))

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
x=Solution()
x.plusOne([7,9])