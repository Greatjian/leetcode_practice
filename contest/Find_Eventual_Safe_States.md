# 802. Find Eventual Safe States

In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

Example:

    Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    Output: [2,4,5,6]
    Here is a diagram of the above graph.
    
## Method:

Note:

- graph will have length at most 10000.
- The number of edges in the graph will not exceed 32000.
- Each graph[i] will be a sorted list of different integers, chosen within the range [0, graph.length - 1].

## Method:

tle:

    class Solution(object):
        def eventualSafeNodes(self, graph):
            """
            :type graph: List[List[int]]
            :rtype: List[int]
            """
            res=[]
            s=set()
            for i in range(len(graph)):
                if i not in s:
                    ns=set()
                    stack=[(i, [i])]
                    while stack:
                        node, path=stack.pop()
                        for neighbor in graph[node]:
                            if neighbor in ns:
                                continue
                            if neighbor in path:
                                for p in path:
                                    ns.add(p)
                                continue
                            stack.append((neighbor, path+[neighbor]))
                    s|=ns
            return [i for i in range(len(graph)) if i not in s]
            
## Solution:

topological sort using indegree:

    class Solution(object):
        def eventualSafeNodes(self, graph):
            """
            :type graph: List[List[int]]
            :rtype: List[int]
            """
            res=[]
            queue=collections.deque()
            d=collections.defaultdict(set)
            indegree=[0]*len(graph)
            for i in range(len(graph)):
                if not graph[i]:
                    queue.append(i)
                for j in graph[i]:
                    d[j].add(i)
                    indegree[i]+=1
            while queue:
                node=queue.popleft()
                res.append(node)
                for neighbor in d[node]:
                    indegree[neighbor]-=1
                    if indegree[neighbor]==0:
                        queue.append(neighbor)
            return sorted(res)
            
using dfs to test cycle:

    class Solution(object):
        def eventualSafeNodes(self, graph):
            """
            :type graph: List[List[int]]
            :rtype: List[int]
            """
            def dfs(i):
                if visited[i]==2:
                    return False
                if visited[i]==1:
                    return True
                visited[i]=1
                for neighbor in graph[i]:
                    if dfs(neighbor):
                        return True
                visited[i]=2
                return False
            
            visited=[0]*len(graph)
            return [i for i in range(len(graph)) if not dfs(i)]