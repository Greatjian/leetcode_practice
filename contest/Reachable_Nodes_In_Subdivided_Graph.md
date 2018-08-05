# 886. Reachable Nodes In Subdivided Graph

Starting with an undirected graph (the "original graph") with nodes from 0 to N-1, subdivisions are made to some of the edges.

The graph is given as follows: edges[k] is a list of integer pairs (i, j, n) such that (i, j) is an edge of the original graph,

and n is the total number of new nodes on that edge. 

Then, the edge (i, j) is deleted from the original graph, n new nodes (x_1, x_2, ..., x_n) are added to the original graph,

and n+1 new edges (i, x_1), (x_1, x_2), (x_2, x_3), ..., (x_{n-1}, x_n), (x_n, j) are added to the original graph.

Now, you start at node 0 from the original graph, and in each move, you travel along one edge. 

Return how many nodes you can reach in at most M moves.

 

Example 1:

    Input: edges = [[0,1,10],[0,2,1],[1,2,2]], M = 6, N = 3
    Output: 13
    Explanation: 
    The nodes that are reachable in the final graph after M = 6 moves are indicated below.

Example 2:

    Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], M = 10, N = 4
    Output: 23
 

Note:

- 0 <= edges.length <= 10000
- 0 <= edges[i][0] < edges[i][1] < N
- There does not exist any i != j for which edges[i][0] == edges[j][0] and edges[i][1] == edges[j][1].
- The original graph has no parallel edges.
- 0 <= edges[i][2] <= 10000
- 0 <= M <= 10^9
- 1 <= N <= 3000

## Method:

To reach more nodes, we need a greedy way using heap (dijkstra's algorithm).

It need to check visited twice since same nodes might be push into the heap multiple times.

To record the shared edges starting from two neighbors, we could change the length of edges along the way,
or use an extra dict to record the distance:


    class Solution(object):
        def reachableNodes(self, edges, M, N):
            """
            :type edges: List[List[int]]
            :type M: int
            :type N: int
            :rtype: int
            """
            d=collections.defaultdict(dict)
            for e1, e2, c in edges:
                d[e1][e2]=c
                d[e2][e1]=c
            visited=set()
            res=0
            hp=[[0, 0]]
            while hp:
                move, node=heapq.heappop(hp)
                if node in visited:
                    continue
                visited.add(node)
                for nei in d[node]:
                    cost=d[node][nei]
                    if nei not in visited and move+cost+1<=M:
                        heapq.heappush(hp, [move+cost+1, nei])
                    d[nei][node]-=min(M-move, cost)
                    res+=min(M-move, cost)
            return res+len(visited)

           
extra dict:            

            
    class Solution(object):
        def reachableNodes(self, edges, M, N):
            """
            :type edges: List[List[int]]
            :type M: int
            :type N: int
            :rtype: int
            """
            d=collections.defaultdict(list)
            for e1, e2, c in edges:
                d[e1].append([e2, c])
                d[e2].append([e1, c])
            d1={}
            visited=set()
            res=0
            hp=[[0, 0]]
            while hp:
                move, node=heapq.heappop(hp)
                if node in visited:
                    continue
                visited.add(node)
                for nei, cost in d[node]:
                    if nei not in visited:
                        if move+cost+1>M:
                            d1[(node, nei)]=M-move
                            res+=M-move
                        else:
                            heapq.heappush(hp, [move+cost+1, nei])
                            # print node, nei, cost
                            res+=cost
                    elif (nei, node) in d1:
                        res+=min(M-move, cost-d1[(nei, node)])
            return res+len(visited)