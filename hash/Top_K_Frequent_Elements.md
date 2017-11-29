# 347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

For example,

    Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
- You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
- Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

## Method:

sort O(nlogn):

    class Solution(object):
        def topKFrequent(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: List[int]
            """
            d=collections.Counter(nums)
            return sorted(d.keys(), key=lambda i:d[i], reverse=True)[:k]
            
using heap O(nlogn):

    class Solution(object):
        def topKFrequent(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: List[int]
            """
            d=collections.Counter(nums)
            hp=[]
            for i in d.keys():
                heapq.heappush(hp, (-d[i], i))
            return [heapq.heappop(hp)[1] for _ in range(k)]
            
using heap O(nlogk):

    class Solution(object):
        def topKFrequent(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: List[int]
            """
            d=collections.Counter(nums)
            hp=[]
            for i in d.keys():
                if len(hp)<k:
                    heapq.heappush(hp, (d[i], i))
                elif len(hp)==k and d[i]>hp[0][0]:
                    heapq.heappushpop(hp, (d[i], i))
            return [heapq.heappop(hp)[1] for _ in range(k)][::-1]
