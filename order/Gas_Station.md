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

greedy:

    class Solution(object):
        def canCompleteCircuit(self, gas, cost):
            """
            :type gas: List[int]
            :type cost: List[int]
            :rtype: int
            """
            extraCost, curGas=0, 0
            res=0
            for i in range(len(gas)):
                curGas+=gas[i]-cost[i]
                if curGas<0:
                    res=i+1
                    extraCost+=curGas
                    curGas=0
            return res if curGas+extraCost>=0 else -1
            
two pointers:

    class Solution(object):
        def canCompleteCircuit(self, gas, cost):
            """
            :type gas: List[int]
            :type cost: List[int]
            :rtype: int
            """
            start, end = len(cost)-1, 0
            s = gas[start]-cost[start]
            while end < start:
                if s>=0:
                    s += gas[end]-cost[end]
                    end += 1
                else:
                    start -= 1
                    s += gas[start]-cost[start]
            return start if s>=0 else -1