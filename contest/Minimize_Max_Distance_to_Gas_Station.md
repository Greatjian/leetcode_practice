# 774. Minimize Max Distance to Gas Station

On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1], where N = stations.length.

Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.

Return the smallest possible value of D.

Example:

    Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
    Output: 0.500000

Note:

- stations.length will be an integer in range [10, 2000].
- stations[i] will be an integer in range [0, 10^8].
- K will be an integer in range [1, 10^6].
- Answers within 10^-6 of the true value will be accepted as correct.

## Method:

binary search:

    class Solution(object):
        def minmaxGasDist(self, stations, K):
            """
            :type stations: List[int]
            :type K: int
            :rtype: float
            """
            
            def valid(length):
                return sum(int ((stations[i]-stations[i-1])/length) for i in range(1, len(stations)))<=K
            
            lo, hi=0, stations[-1]
            while hi-lo>10**-6:
                mid=(lo+hi)*1.0/2
                if valid(mid):
                    hi=mid
                else:
                    lo=mid
            return lo