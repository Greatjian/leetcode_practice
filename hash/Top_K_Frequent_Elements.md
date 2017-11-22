# 347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

For example,

    Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
- You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
- Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

## Method:

count+sort:

    class Solution(object):
        def topKFrequent(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: List[int]
            """
            d=collections.Counter(nums)
            t=[]
            for key in d:
                t.append((key, d[key]))
            t.sort(key=lambda x: x[1], reverse=True)
            return [i[0] for i in t[:k]]
            
         // t=sorted(d.items(), key=lambda x:x[1], reverse=True)
