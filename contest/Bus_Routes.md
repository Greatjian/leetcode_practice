# 815. Bus Routes

We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

Example:

    Input: 
    routes = [[1, 2, 7], [3, 6, 7]]
    S = 1
    T = 6
    Output: 2

    Explanation: 
    The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

Note:

- 1 <= routes.length <= 500.
- 1 <= routes[i].length <= 500.
- 0 <= routes[i][j] < 10 ^ 6.

## Method:

bfs, tle(5/45):

    class Solution(object):
        def numBusesToDestination(self, routes, S, T):
            """
            :type routes: List[List[int]]
            :type S: int
            :type T: int
            :rtype: int
            """
            d=collections.defaultdict(list)
            for route in routes:
                for i in route:
                    for j in route:
                        if i!=j:
                            d[i].append(j)
            res=0
            queue=collections.deque([(S, [S])])
            while queue:
                for _ in range(len(queue)):
                    node, path=queue.popleft()
                    if node==T:
                        return res
                    for n in d[node]:
                        if n not in path:
                            queue.append((n, path+[n]))
                res+=1
            return -1
            
bfs+memo, tle(43/45):

    class Solution(object):
        def numBusesToDestination(self, routes, S, T):
            """
            :type routes: List[List[int]]
            :type S: int
            :type T: int
            :rtype: int
            """
            d=collections.defaultdict(set)
            for route in routes:
                for i in route:
                    for j in route:
                        if i!=j:
                            d[i].add(j)
            s=set()
            res=0
            queue=collections.deque([S])
            while queue:
                for _ in range(len(queue)):
                    node=queue.popleft()
                    if node==T:
                        return res
                    if node not in s:
                        s.add(node)
                        for n in d[node]:
                            queue.append(n)
                res+=1
            return -1
            
## Solution:

record bus in set instead of nodes, save time:

    class Solution(object):
        def numBusesToDestination(self, routes, S, T):
            """
            :type routes: List[List[int]]
            :type S: int
            :type T: int
            :rtype: int
            """
            d=collections.defaultdict(set)
            for i, v in enumerate(routes):
                for route in v:
                    d[route].add(i)
            s=set()
            res=0
            queue=collections.deque([S])
            while queue:
                for _ in range(len(queue)):
                    node=queue.popleft()
                    if node==T:
                        return res
                    for bus in d[node]:
                        if bus not in s:
                            s.add(bus)
                            for n in routes[bus]:
                                queue.append(n)
                res+=1
            return -1