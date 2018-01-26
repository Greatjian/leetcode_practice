# 163. Missing Ranges

Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

    For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99
    
    return ["2", "4->49", "51->74", "76->99"].
    
## Method:

    class Solution(object):
        def findMissingRanges(self, nums, lower, upper):
            """
            :type nums: List[int]
            :type lower: int
            :type upper: int
            :rtype: List[str]
            """
            res=[]
            for num in nums:
                if num-lower==1:
                    res.append(str(lower))
                elif num-lower>1:
                    res.append(str(lower)+"->"+str(num-1))
                lower=num+1
            if upper==lower:
                res.append(str(lower))
            elif upper-lower>0:
                res.append(str(lower)+"->"+str(upper))
            return res