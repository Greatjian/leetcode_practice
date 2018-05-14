# 834. Sum of Distances in Tree

An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.

The ith edge connects nodes edges[i][0] and edges[i][1] together.

Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.

Example 1:

    Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    Output: [8,12,6,10,10,10]

    Explanation: 
    Here is a diagram of the given tree:

      0
     / \
    1   2
       /|\
      3 4 5

    We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
    equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.

Note: 1 <= N <= 10000

## Method:

Use bfs to get sum for 0, get path along the way

then compute other distances using the path

O(n^2), tle (64/69):

    class Solution(object):
        def sumOfDistancesInTree(self, N, edges):
            """
            :type N: int
            :type edges: List[List[int]]
            :rtype: List[int]
            """
            g=[[] for i in range(N)]
            path={}
            for e in edges:
                g[e[0]].append(e[1])
                g[e[1]].append(e[0])
            d=[[0]*N for i in range(N)]
            s=set()
            queue=collections.deque([[0, [0]]])
            while queue:
                for _ in range(len(queue)):
                    node, root=queue.popleft()
                    path[node]=root
                    for j in range(len(root)-1):
                        d[root[j]][node]=len(root)-j-1
                        d[node][root[j]]=len(root)-j-1
                    for n in g[node]:
                        if n not in s:
                            s.add(n)
                            queue.append([n, root+[n]])

            for i in range(N):
                for j in range(N):
                    if i!=j and d[i][j]==0:
                        for index in range(len(path[i])-1, -1, -1):
                            if index<len(path[j]) and path[i][index]==path[j][index]:
                                dist=len(path[i]+path[j])-index*2-2
                                d[i][j]=d[j][i]=dist
                                break
                                
            return [sum(d[i]) for i in range(N)]

## Solution:

dfs1: get count for all nodes and sum for node 0.

dfs2: get sum for other nodes using node 0.

Time complexity: O(n):

    class Solution(object):
        def sumOfDistancesInTree(self, N, edges):
            """
            :type N: int
            :type edges: List[List[int]]
            :rtype: List[int]
            """
            graph=collections.defaultdict(list)
            for e in edges:
                graph[e[0]].append(e[1])
                graph[e[1]].append(e[0])
            
            cnt=[1]*N
            ans=[0]*N
            
            def dfs1(start, s=set()):
                s.add(start)
                for n in graph[start]:
                    if n not in s:
                        dfs1(n, s)
                        cnt[start]+=cnt[n]
                        ans[start]+=ans[n]+cnt[n]
                        
            def dfs2(start, s=set()):
                s.add(start)
                for n in graph[start]:
                    if n not in s:
                        ans[n]=ans[start]-2*cnt[n]+N
                        dfs2(n, s)
            
            dfs1(0)
            dfs2(0)
            return ans