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

    class Solution(object):
        def numBusesToDestination(self, routes, S, T):
            """
            :type routes: List[List[int]]
            :type S: int
            :type T: int
            :rtype: int
            """
            if S==T:
                return 0
            routes = map(set, routes)
            d=collections.defaultdict(set)
            for i in range(len(routes)):
                for j in range(i+1, len(routes)):
                    if any (bus in routes[j] for bus in routes[i]):
                        d[i].add(j)
                        d[j].add(i)
            
            start, end=set(), set()
            queue=collections.deque()
            for i in range(len(routes)):
                if S in routes[i]:
                    start.add(i)
                    queue.append([i, 1])
                if T in routes[i]:
                    end.add(i)
                    
            while queue:
                node, depth=queue.popleft()
                if node in end:
                    return depth
                for n in d[node]:
                    if n not in start:
                        start.add(n)
                        queue.append([n, depth+1])
            return -1