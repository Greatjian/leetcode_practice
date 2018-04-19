# 818. Race Car

Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).

When you get an instruction "A", your car does the following: position += speed, speed *= 2.

When you get an instruction "R", your car does the following: if your speed is positive then speed = -1 , otherwise speed = 1.  (Your position stays the same.)

For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.

Now for some target position, say the length of the shortest sequence of instructions to get there.

Example 1:

    Input: 
    target = 3
    Output: 2

    Explanation: 
    The shortest instruction sequence is "AA".
    Your position goes from 0->1->3.

Example 2:

    Input: 
    target = 6
    Output: 5

    Explanation: 
    The shortest instruction sequence is "AAARA".
    Your position goes from 0->1->3->7->7->6.
 
Note:

- 1 <= target <= 10000.

## Solution:

bfs, tle (48/53):

    class Solution(object):
        def racecar(self, target):
            """
            :type target: int
            :rtype: int
            """
            queue=collections.deque([(0, 1)])
            res=0
            s=set([(0, 1)])
            while queue:
                for _ in range(len(queue)):
                    pos, spd=queue.popleft()
                    if pos==target:
                        return res
                    A=(pos+spd, spd*2)
                    R=(pos, (-1 if spd>0 else 1))
                    for i in [A, R]:
                        if i not in s and i[0]<2*target:
                            s.add(i)
                            queue.append(i)
                res+=1
            return -1
                
dp:
                
    class Solution(object):
        def racecar(self, target):
            """
            :type target: int
            :rtype: int
            """
            dp = [0, 1, 4] + [float('inf')] * target
            for t in xrange(3, target + 1):
                k = t.bit_length()
                if t == 2**k - 1:
                    dp[t] = k
                    continue
                for j in xrange(k - 1):
                    dp[t] = min(dp[t], dp[t - 2**(k - 1) + 2**j] + k - 1 + j + 2)
                if 2**k - 1 - t < t:
                    dp[t] = min(dp[t], dp[2**k - 1 - t] + k + 1)
            return dp[target]
                