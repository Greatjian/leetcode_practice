# 787. Cheapest Flights Within K Stops

There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and fights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:

    Input: 
    n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0, dst = 2, k = 1
    Output: 200

    Explanation: 
    The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example 2:

    Input: 
    n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0, dst = 2, k = 0
    Output: 500

    Explanation: 
    The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

Note:

- The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
- The size of flights will be in range [0, n * (n - 1) / 2].
- The format of each flight will be (src, dst, price).
- The price of each flight will be in the range [1, 10000].
- k is in the range of [0, n - 1].
- There will not be any duplicated flights or self cycles.

## Method:

bfs, tle:

    class Solution(object):
        def findCheapestPrice(self, n, flights, src, dst, K):
            """
            :type n: int
            :type flights: List[List[int]]
            :type src: int
            :type dst: int
            :type K: int
            :rtype: int
            """
            d=collections.defaultdict(list)
            for f in flights:
                d[f[0]].append([f[1], f[2]])
            queue=collections.deque([(0, src)])
            k=-2
            res=float('inf')
            while queue:
                for _ in range(len(queue)):
                    price, stop=queue.popleft()
                    if stop==dst:
                        res=min(res, price)
                    for nextstop, nextprice in d[stop]:
                        queue.append((price+nextprice, nextstop))
                k+=1
                if k==K:
                    break
            return res if res!=float('inf') else -1
            
modified:

    class Solution(object):
        def findCheapestPrice(self, n, flights, src, dst, K):
            """
            :type n: int
            :type flights: List[List[int]]
            :type src: int
            :type dst: int
            :type K: int
            :rtype: int
            """
            d=collections.defaultdict(list)
            d2={}
            for f in flights:
                d[f[0]].append([f[1], f[2]])
            queue=collections.deque([(0, src)])
            d2[src]=0
            k=-1
            while queue:
                for _ in range(len(queue)):
                    price, stop=queue.popleft()
                    for nextstop, nextprice in d[stop]:
                        if nextstop not in d2 or d2[nextstop]>price+nextprice:
                            d2[nextstop]=price+nextprice
                            queue.append((price+nextprice, nextstop))
                k+=1
                if k==K:
                    break
            return d2[dst] if dst in d2 else -1
            
## Solution:

Dijkstra's algorithm using pq:

    class Solution(object):
        def findCheapestPrice(self, n, flights, src, dst, K):
            """
            :type n: int
            :type flights: List[List[int]]
            :type src: int
            :type dst: int
            :type K: int
            :rtype: int
            """
            d=collections.defaultdict(list)
            p=[float('inf')]*n
            p[src]=0
            for f in flights:
                d[f[0]].append([f[1], f[2]])
            pq=[(0, src, -2)]
            while pq:
                price, stop, k=heapq.heappop(pq)
                if k==K:
                    continue
                if stop==dst:
                    return price
                for nextstop, nextprice in d[stop]:
                    if p[nextstop]>price+nextprice:
                        p[nextstop]=price+nextprice
                        heapq.heappush(pq, (price+nextprice, nextstop, k+1))
            return -1