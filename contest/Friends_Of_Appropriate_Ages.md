# 825. Friends Of Appropriate Ages

Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

    Example 1:
    
    Input: [16,16]
    Output: 2
    Explanation: 2 people friend request each other.

    Example 2:
    
    Input: [16,17,18]
    Output: 2
    Explanation: Friend requests are made 17 -> 16, 18 -> 17.

    Example 3:
    
    Input: [20,30,100,110,120]
    Output: 
    Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
 

Notes:

- 1 <= ages.length <= 20000.
- 1 <= ages[i] <= 120.

## Method:

rangeSum -> preSum:

    class Solution(object):
        def numFriendRequests(self, ages):
            """
            :type ages: List[int]
            :rtype: int
            """
            cnt=0
            dp=[0]*121
            for i in range(len(ages)):
                dp[ages[i]]+=1
            for i in range(1, len(dp)):
                dp[i]+=dp[i-1]
            for age in ages:
                cnt+=(dp[age]-dp[age/2+7]-1 if dp[age]-dp[age/2+7]-1>0 else 0)
            return cnt
            
## Solution:

    class Solution(object):
        def numFriendRequests(self, ages):
            """
            :type ages: List[int]
            :rtype: int
            """
            cnt=0
            dp=[0]*121
            for i in range(len(ages)):
                dp[ages[i]]+=1
            for i in range(15, 121):
                for j in range(i/2+8, i+1):
                    cnt+=dp[i]*dp[j]
                    if i==j:
                        cnt-=dp[j]
            return cnt