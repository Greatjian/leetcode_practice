# 599. Minimum Index Sum of Two Lists

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:

    Input:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    Output: ["Shogun"]
    Explanation: The only restaurant they both like is "Shogun".

Example 2:

    Input:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["KFC", "Shogun", "Burger King"]
    Output: ["Shogun"]
    Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

Note:
- The length of both lists will be in the range of [1, 1000].
- The length of strings in both lists will be in the range of [1, 30].
- The index is starting from 0 to the list length minus 1.
- No duplicates in both lists.

## Method:

    class Solution(object):
        def findRestaurant(self, list1, list2):
            """
            :type list1: List[str]
            :type list2: List[str]
            :rtype: List[str]
            """
            d=collections.defaultdict(list)
            for idx, value in enumerate(list1):
                d[value].append(idx)
            for idx, value in enumerate(list2):
                d[value].append(idx)
            m=float('inf')
            res=[]
            for i in d:
                if len(d[i])>1:
                    if sum(d[i])<m:
                        m=sum(d[i])
                        res=[i]
                    elif sum(d[i])==m:
                        res.append(i)
            return res
            
or one loop for list1 and check for list2:

    class Solution(object):
        def findRestaurant(self, list1, list2):
            """
            :type list1: List[str]
            :type list2: List[str]
            :rtype: List[str]
            """
            d={}
            for idx, value in enumerate(list1):
                d[value]=idx
            m=float('inf')
            res=[]
            for idx, val in enumerate(list2):
                if val in d:
                    if d[val]+idx<m:
                        m=d[val]+idx
                        res=[val]
                    elif d[val]+idx==m:
                        res.append(val)
            return res