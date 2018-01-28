# 215. Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

    For example,

    Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
- You may assume k is always valid, 1 ≤ k ≤ array's length.

## Method:

minheap, O(n+(n-k)logn):

    class Solution(object):
        def findKthLargest(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
            heapq.heapify(nums)
            for i in range(len(nums)-k):
                heapq.heappop(nums)
            return heapq.heappop(nums)
            
O(k+(n-k)logk):

    class Solution(object):
        def findKthLargest(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
            pq=[]
            for num in nums:
                heapq.heappush(pq, num)
                if len(pq)>k:
                    heapq.heappop(pq)
            return pq[0]
            
sort, O(nlogn):

    class Solution(object):
        def findKthLargest(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
            return sorted(nums)[len(nums)-k]
            
quicksort using partition, O(n) average, O(n^2) worst case:

    class Solution(object):
        def findKthLargest(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
        
            def partition(A, start, end):
                pivot=A[end]
                i=start
                for cur in range(start, end+1):
                    if A[cur]<pivot:
                        A[i], A[cur]=A[cur], A[i]
                        i+=1
                A[i], A[end]=A[end], A[i]
                return i
            
            start, end=0, len(nums)-1
            while start<=end:
                # random.shuffle(nums)
                pivot_pos=partition(nums, start, end)
                if pivot_pos==len(nums)-k:
                    return nums[len(nums)-k]
                if pivot_pos>len(nums)-k:
                    end=pivot_pos-1
                else:
                    start=pivot_pos+1