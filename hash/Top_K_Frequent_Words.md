# 692. Top K Frequent Words

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:

    Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
    Output: ["i", "love"]
    Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

    Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
    Output: ["the", "is", "sunny", "day"]
    Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
        with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:
- You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
- Input words contain only lowercase letters.

Follow up:
- Try to solve it in O(n log k) time and O(n) extra space.

## Method:

wrong answer at:

> ["aaa","aa","a"]
>
> 1

    class Solution(object):
        def topKFrequent(self, words, k):
            """
            :type words: List[str]
            :type k: int
            :rtype: List[str]
            """
            d=collections.Counter(words)
            return sorted(d.keys(), key=lambda i: d[i], reverse=True)[:k]
            
修改, O(nlogn)：

    class Solution(object):
        def topKFrequent(self, words, k):
            """
            :type words: List[str]
            :type k: int
            :rtype: List[str]
            """
            d=collections.Counter(words)
            return sorted(d.keys(), key=lambda i: (-d[i], i))[:k]
            
## Solution:

O(nlogn) using heap:

    class Solution(object):
        def topKFrequent(self, words, k):
            """
            :type words: List[str]
            :type k: int
            :rtype: List[str]
            """
            d=collections.Counter(words)
            hp, res=[], []
            for i in d.keys():
                heapq.heappush(hp, (-d[i], i))
            for i in range(k):
                res.append(heapq.heappop(hp)[1])
            return res
            
using heapq.heapify(list):

    class Solution(object):
        def topKFrequent(self, words, k):
            """
            :type words: List[str]
            :type k: int
            :rtype: List[str]
            """
            d=collections.Counter(words)
            hp=[(-d[i], i) for i in d.keys()]
            heapq.heapify(hp)
            res=[]
            for i in range(k):
                res.append(heapq.heappop(hp)[1])
            return res
            
O(nlogk) solution, change ways of comparing:

[lala](https://discuss.leetcode.com/topic/107256/python-3-solution-with-o-nlogk-and-o-n)