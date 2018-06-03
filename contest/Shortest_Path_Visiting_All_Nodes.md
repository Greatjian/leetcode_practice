# 847. Shortest Path Visiting All Nodes

An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.

graph.length = N, and j != i is in the list graph[i] exactly once, if and only if nodes i and j are connected.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

Example 1:

    Input: [[1,2,3],[0],[0],[0]]
    Output: 4
    Explanation: One possible path is [1,0,2,0,3]

Example 2:

    Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
    Output: 4
    Explanation: One possible path is [0,1,4,2,3]
 
Note:

- 1 <= graph.length <= 12
- 0 <= graph[i].length < graph.length

## Solution:

O(N*2^N):

    class Solution(object):
        def shortestPathLength(self, graph):
            """
            :type graph: List[List[int]]
            :rtype: int
            """
            l=len(graph)
            
            # dp[state][node] for steps
            dp=[[float('inf')]*l for _ in range(1<<l)]
            
            # (node, state)
            queue=collections.deque()
            for i in range(l):
                queue.append((i, 1<<i))
                dp[1<<i][i]=0
                
            while queue:
                node, state=queue.popleft()
                for n in graph[node]:
                    newState=state|(1<<n)
                    if dp[newState][n]>dp[state][node]+1:
                        dp[newState][n]=dp[state][node]+1
                        queue.append((n, newState))
                            
            return min(dp[-1])