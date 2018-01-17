# 754. Reach a Number

You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:

    Input: target = 3
    Output: 2
    
    Explanation:
    - On the first move we step from 0 to 1.
    - On the second step we step from 1 to 3.

Example 2:

    Input: target = 2
    Output: 3

    Explanation:
    - On the first move we step from 0 to 1.
    - On the second move we step  from 1 to -1.
    - On the third move we step from -1 to 2.

Note:
- target will be a non-zero integer in the range [-10^9, 10^9].

## Method:

tle:

    class Solution(object):
        def reachNumber(self, target):
            """
            :type target: int
            :rtype: int
            """
            d=collections.defaultdict(list)
            d[0]=[0]
            step=0
            while True:
                for i in d[step]:
                    if i+step+1 not in d.values():
                        d[step+1].append(i+step+1)
                    if i-step-1 not in d.values():
                        d[step+1].append(i-step-1)
                    if i+step+1==target or i-step-1==target:
                        return step+1
                step+=1
                
## Solution:

求和后改符号：

    class Solution(object):
        def reachNumber(self, target):
            """
            :type target: int
            :rtype: int
            """
            target=abs(target)
            s, res=0, 0
            while s<target:
                res+=1
                s+=res
            if s==target or (s-target)%2==0:
                return res
            res+=1
            s+=res
            if (s-target)%2==0:
                return res
            return res+1
