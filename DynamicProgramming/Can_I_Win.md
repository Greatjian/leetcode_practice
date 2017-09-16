# 464. Can I Win

In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

    Input:
    maxChoosableInteger = 10
    desiredTotal = 11
    
    Output:
    false

Explanation:

    No matter which integer the first player choose, the first player will lose.
    The first player can choose an integer from 1 up to 10.
    If the first player choose 1, the second player can only choose integers from 2 up to 10.
    The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
    Same with other integers chosen by the first player, the second player will always win.

## Method:
memo记录搜索过状态，backtracking:

    class Solution(object):
        def canIWin(self, maxChoosableInteger, desiredTotal):
            """
            :type maxChoosableInteger: int
            :type desiredTotal: int
            :rtype: bool
            """
            if (1 + maxChoosableInteger) * maxChoosableInteger/2 < desiredTotal:
                return False
            self.memo = {}
            return self.helper(range(1, maxChoosableInteger + 1), desiredTotal)
    
            
        def helper(self, nums, desiredTotal):
            
            hash = str(nums)
            if hash in self.memo:
                return self.memo[hash]
            
            if nums[-1] >= desiredTotal:
                return True
                
            for i in range(len(nums)):
                if not self.helper(nums[:i] + nums[i+1:], desiredTotal - nums[i]):
                    self.memo[hash]= True
                    return True
                
            self.memo[hash] = False
            return False
            
## Solution:
位运算+记忆化搜索：

state表示当前已经选择了哪些数字，state的第i位为1时，表示选择了数字i+1。

通过&判断是否重复，|添加新元素。

对方下步f则我此步t；若我此步所有可能均不是t，则为f。

    class Solution(object):
        def canIWin(self, maxChoosableInteger, desiredTotal):
            """
            :type maxChoosableInteger: int
            :type desiredTotal: int
            :rtype: bool
            """
            if desiredTotal<=maxChoosableInteger:
                return True;
            if maxChoosableInteger*(maxChoosableInteger+1)/2<desiredTotal:
                return False;
            m={}
            return self.canWin(desiredTotal, maxChoosableInteger, 0, m)
        
        def canWin(self, total, n, state, m):
            if state in m:
                return m[state]
            for i in range(0,n):
                if state&(1<<i)!=0:
                    continue
                if total<=i+1 or not self.canWin(total-(i+1), n, state|(1<<i), m):
                    m[state]=True
                    return True
            m[state]=False
            return False            