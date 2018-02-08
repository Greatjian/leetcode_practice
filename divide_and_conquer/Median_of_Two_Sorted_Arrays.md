# 004. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

    nums1 = [1, 3]
    nums2 = [2]
    
    The median is 2.0

Example 2:

    nums1 = [1, 2]
    nums2 = [3, 4]
    
    The median is (2 + 3)/2 = 2.5
    
## Method:

top k, O(logk):

    class Solution(object):
        def findMedianSortedArrays(self, nums1, nums2):
            """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: float
            """
            k=(len(nums1)+len(nums2)+1)/2
            if (len(nums1)+len(nums2))%2:
                return self.helper(nums1, nums2, k)
            else:
                return (self.helper(nums1, nums2, k)+self.helper(nums1, nums2, k+1))/2.0
            
        def helper(self, num1, num2, k):
            len1, len2=len(num1), len(num2)
            if len1 > len2:
                return  self.helper(num2, num1, k)
            if len1 == 0:
                return (num2[k-1])
            if k == 1:
                return (min(num1[0], num2[0]))
            m = min(k/2, len1)
            n = k-m
            if num1[m-1] < num2[n-1]:
                return self.helper(num1[m:], num2, k-m)
            elif num1[m-1] > num2[n-1]:
                return self.helper(num1, num2[n:], k-n)
            else:
                return num1[m-1]
                
## Solution:

cut into halves:

    class Solution(object):
        def findMedianSortedArrays(self, nums1, nums2):
            """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: float
            """
            n1, n2=len(nums1), len(nums2)
            if n1<n2:
                return self.findMedianSortedArrays(nums2, nums1)
            lo, hi=0, 2*n2
            while lo<=hi:
                mid2=(lo+hi)/2
                mid1=n1+n2-mid2
                l1=(nums1[(mid1-1)/2] if mid1!=0 else float('-inf'))
                r1=(nums1[mid1/2] if mid1!=2*n1 else float('inf'))
                l2=(nums2[(mid2-1)/2] if mid2!=0 else float('-inf'))
                r2=(nums2[mid2/2] if mid2!=2*n2 else float('inf'))
                if l2>r1:
                    hi=mid2-1
                elif r2<l1:
                    lo=mid2+1
                else:
                    return (max(l1, l2)+min(r1, r2))/2.0
