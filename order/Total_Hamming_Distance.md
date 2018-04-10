# 477. Total Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:

    Input: 4, 14, 2
    
    Output: 6
    
    Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
    showing the four bits relevant in this case). So the answer will be:
    HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

Note:
- Elements of the given array are in the range of 0 to 10^9
- Length of the array will not exceed 10^4.

## Method:

count and add, O(n^2) tle:

    class Solution(object):
        def totalHammingDistance(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            def countDistance(x, y):
                xor=x^y
                cnt=0
                while xor:
                    cnt+=xor%2
                    xor/=2
                return cnt
            
            res=0
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    res+=countDistance(nums[i], nums[j])
            return res
            
## Solution:

cnt each bits, O(n):

    class Solution(object):
        def totalHammingDistance(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            res=0
            for i in range(32):
                cnt=0
                for j in range(len(nums)):
                    cnt+=(nums[j]>>i)%2
                res+=cnt*(len(nums)-cnt)
            return res