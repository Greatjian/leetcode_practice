# 871. Minimum Number of Refueling Stops

A car travels from a starting position to a destination which is target miles east of the starting position.

Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east of the starting position, and has station[i][1] liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

What is the least number of refueling stops the car must make in order to reach its destination?  If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.  If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

Example 1:

    Input: target = 1, startFuel = 1, stations = []
    Output: 0
    Explanation: We can reach the target without refueling.

Example 2:

    Input: target = 100, startFuel = 1, stations = [[10,100]]
    Output: -1
    Explanation: We can't reach the target (or even the first gas station).

Example 3:

    Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
    Output: 2
    Explanation: 
    We start with 10 liters of fuel.
    We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
    Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
    and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
    We made 2 refueling stops along the way, so we return 2.
 

Note:

- 1 <= target, startFuel, stations[i][1] <= 10^9
- 0 <= stations.length <= 500
- 0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target

## Method:

try to use dp at contest. dp[i] is a dictionary at stations[i], with (cnt, dist) is largest dist at each cnt refuel.

bad representation, could not solve the problem at contest.

    class Solution(object):
        def minRefuelStops(self, target, startFuel, stations):
            """
            :type target: int
            :type startFuel: int
            :type stations: List[List[int]]
            :rtype: int
            """
            res=float('inf')
            dp=[[1]]*(len(stations)+1)
            for i in range(len(dp)):
                dp[i]={}
            dp[0]={0: startFuel}
            for i in range(len(stations)):
                for cnt, curFuel in dp[i].items():
                    if (0 if i==0 else stations[i-1][0])+curFuel>=target:
                        res=min(res, cnt)
                    if curFuel<stations[i][0]-(0 if i==0 else stations[i-1][0]):
                        continue
                    if cnt+1 in dp[i+1] and dp[i+1][cnt]>=curFuel-(stations[i][0]-(0 if i==0 else stations[i-1][0])):
                        continue
                    dp[i+1][cnt+1]=curFuel-(stations[i][0]-(0 if i==0 else stations[i-1][0]))+stations[i][1]
                    if stations[i][0]+curFuel-(stations[i][0]-(0 if i==0 else stations[i-1][0]))+stations[i][1]>=target:
                        res=min(res, cnt+1)
            # print dp
            if not stations and startFuel>=target:
                return 0
            if res==float('inf'):
                return -1
            return res
            
## Solution:

dp[i] represent largest dist at ith refuel, with 0 at starting point

it's similar to 0/1 knapsack problem, time complexity is O(n^2):

    class Solution(object):
        def minRefuelStops(self, target, startFuel, stations):
            """
            :type target: int
            :type startFuel: int
            :type stations: List[List[int]]
            :rtype: int
            """
            dp=[float('-inf')]*(len(stations)+1)
            dp[0]=startFuel
            for i in range(len(stations)):
                for j in range(i, -1, -1):
                    if dp[j]>=stations[i][0]:
                        dp[j+1]=max(dp[j+1], dp[j]+stations[i][1])
            for i in range(len(dp)):
                if dp[i]>=target:
                    return i
            return -1
            
Using heap is a better way for greedy algorithm, since dist is updated using the maximum fuel from the past stations.

time complexity is O(nlogn):

    class Solution(object):
        def minRefuelStops(self, target, startFuel, stations):
            """
            :type target: int
            :type startFuel: int
            :type stations: List[List[int]]
            :rtype: int
            """
            queue = []
            dist = startFuel
            res = 0
            idx = 0
            while True:
                while idx < len(stations) and stations[idx][0] <= dist:
                    heapq.heappush(queue, -stations[idx][1])
                    idx+=1
                if dist >= target: 
                    return res
                if not queue: 
                    return -1
                dist += -heapq.heappop(queue)
                res+=1