# 451. Sort Characters By Frequency

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

    Input:
    "tree"
    
    Output:
    "eert"
    
    Explanation:
    'e' appears twice while 'r' and 't' both appear once.
    So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

    Input:
    "cccaaa"
    
    Output:
    "cccaaa"
    
    Explanation:
    Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
    Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
    
    Input:
    "Aabb"
    
    Output:
    "bbAa"
    
    Explanation:
    "bbaA" is also a valid answer, but "Aabb" is incorrect.

Note that 'A' and 'a' are treated as two different characters.

## Method:

    class Solution(object):
        def frequencySort(self, s):
            """
            :type s: str
            :rtype: str
            """
            d=collections.Counter(s)
            return ''.join(sorted(d.elements(), key=lambda i:d[i], reverse=True))
            
or:

    class Solution(object):
        def frequencySort(self, s):
            """
            :type s: str
            :rtype: str
            """
            d=collections.Counter(s)
            s=sorted(d.items(), key=lambda i:i[1], reverse=True)
            return ''.join([i[0]*i[1] for i in s])
            
using heap (push and pop similar to sort):

    class Solution(object):
        def frequencySort(self, s):
            """
            :type s: str
            :rtype: str
            """
            d=collections.Counter(s)
            heap = []
            for key, value in d.items():
                heapq.heappush(heap, (-value, key))
            res = ''
            while heap:
                count, char = heapq.heappop(heap)
                res += char*(-count)
            return res