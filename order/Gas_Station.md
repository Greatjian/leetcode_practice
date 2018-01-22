# 134. Gas Station

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
- The solution is guaranteed to be unique.

## Method:

nice try, but wrong [3, -7, 2, -1, 3]:

    class Solution(object):
        def canCompleteCircuit(self, gas, cost):
            """
            :type gas: List[int]
            :type cost: List[int]
            :rtype: int
            """
            diff=[gas[i]-cost[i] for i in range(len(gas))]
            return diff.index(max(diff)) if sum(diff)>=0 else -1
            
## Solution:

leftSum, curSum:

    class Solution(object):
        def canCompleteCircuit(self, gas, cost):
            """
            :type gas: List[int]
            :type cost: List[int]
            :rtype: int
            """
            leftSum=0
            curSum=0
            res=0
            for i in range(len(gas)):
                curSum+=gas[i]-cost[i]
                if curSum<0:
                    res=i+1
                    leftSum+=curSum
                    curSum=0
            return res if curSum+leftSum>=0 else -1