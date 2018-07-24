# 685. Redundant Connection II

In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:

    Input: [[1,2], [1,3], [2,3]]
    Output: [2,3]
    Explanation: The given directed graph will be like this:
      1
     / \
    v   v
    2-->3

Example 2:

    Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
    Output: [4,1]
    Explanation: The given directed graph will be like this:
    5 <- 1 -> 2
         ^    |
         |    v
         4 <- 3

Note:
- The size of the input 2D-array will be between 3 and 1000.
- Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

## Method:

follow the same idea, but since problem changes from undirected graph to directed graph,
we need to check for following cases:

- node with two parent
- graph has a cycle
- both

we respectively return three candidates as shown below:


    class Node:
        def __init__(self):
            self.parent=self
            self.rank=1
    
    class Solution(object):
        def findRedundantDirectedConnection(self, edges):
            """
            :type edges: List[List[int]]
            :rtype: List[int]
            """
            def find(node):
                if node.parent!=node:
                    node.parent=find(node.parent)
                return node.parent
    
            def union(p, q):
                r1=find(p)
                r2=find(q)
                if r1!=r2:
                    if r2.rank>r1.rank:
                        r1.parent=r2
                    elif r2.rank<r1.rank:
                        r2.parent=r1
                    else:
                        r1.parent=r2
                        r2.rank+=1
    
            d={}
            can={}
            c1, c2, c3=None, None, None
            twoParent=False
            for a, b in edges:
                if a not in d:
                    d[a]=Node()
                if b not in d:
                    d[b]=Node()
                if b in can:
                    twoParent=True
                    c1, c2=can[b], [a, b]
                    continue
                can[b]=[a, b]
                if find(d[a])==find(d[b]):
                    c3=[a, b]
                union(d[a], d[b])
            if twoParent:
                if c3 is not None:
                    return c1
                return c2
            return c3