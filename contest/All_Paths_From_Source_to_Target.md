# 797. All Paths From Source to Target

Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:

    Input: [[1,2], [3], [3], []] 
    Output: [[0,1,3],[0,2,3]] 
  
    Explanation: The graph looks like this:
  
    0--->1
    |    |
    v    v
    2--->3
    There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Note:

- The number of nodes in the graph will be in the range [2, 15].
- You can print different paths in any order, but you should keep the order of nodes inside one path.

## Method:

same node may be added at different depth, wrong answer:

    Input:
    [[4,3,1],[3,2,4],[3],[4],[]]
    Output:
    [[0,1,4],[0,1,2,3,4],[0,4]]
    Expected:
    [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

    class Solution(object):
        def allPathsSourceTarget(self, graph):
            """
            :type graph: List[List[int]]
            :rtype: List[List[int]]
            """
            stack=[(0, [0])]
            res=[]
            s=set()
            while stack:
                node, path=stack.pop()
                if node==len(graph)-1:
                    res.append(path)
                if node not in s:
                    s.add(node)
                    for neighbor in graph[node]:
                        stack.append((neighbor, path+[neighbor]))
            return res
            
change memorization:

    class Solution(object):
        def allPathsSourceTarget(self, graph):
            """
            :type graph: List[List[int]]
            :rtype: List[List[int]]
            """
            stack=[(0, [0])]
            res=[]
            while stack:
                node, path=stack.pop()
                if node==len(graph)-1:
                    res.append(path)
                for neighbor in graph[node]:
                    if neighbor not in path:
                        stack.append((neighbor, path+[neighbor]))
            return res