# 349. Intersection of Two Arrays


Given two arrays, write a function to compute their intersection.

    Example:

    Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
- Each element in the result must be unique.
- The result can be in any order.

## Method：

use set to check:

    class Solution(object):
        def intersection(self, nums1, nums2):
            """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: List[int]
            """
            a = set(nums1)
            b = set(nums2)
            res = []
            for i in a:
                if i in b:
                    res.append(i)
            return res
            
## Solution:

    class Solution(object):
        def intersection(self, nums1, nums2):
            """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: List[int]
            """
            return list(set(nums1) & set(nums2))
            