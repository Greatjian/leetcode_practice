# 837. New 21 Game

Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points, and draws numbers while she has less than K points.  During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.  Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets K or more points.  What is the probability that she has N or less points?

Example 1:

    Input: N = 10, K = 1, W = 10
    Output: 1.00000
    Explanation:  Alice gets a single card, then stops.

Example 2:

    Input: N = 6, K = 1, W = 10
    Output: 0.60000
    Explanation:  Alice gets a single card, then stops.
    In 6 out of W = 10 possibilities, she is at or below N = 6 points.

Example 3:

    Input: N = 21, K = 17, W = 10
    Output: 0.73278

Note:

- 0 <= K <= N <= 10000
- 1 <= W <= 10000
- Answers will be accepted as correct if they are within 10^-5 of the correct answer.
- The judging time limit has been reduced for this question.

## Method:

dp[i]=sum(dp[j] for j in range(i-W, i))

brute force, O(WK), tle (96/146):

    class Solution(object):
        def new21Game(self, N, K, W):
            """
            :type N: int
            :type K: int
            :type W: int
            :rtype: float
            """
                    
            dp=[0.0]*(K+W+1)
            dp[0]=1.0
            for i in range(K):
                for j in range(i+1, i+W+1):
                    dp[j]+=dp[i]/W
            return sum(dp[i] for i in range(K, N+1))
            
maintain a sliding window, pay attention to corner cases, O(K+W):

    class Solution(object):
        def new21Game(self, N, K, W):
            """
            :type N: int
            :type K: int
            :type W: int
            :rtype: float
            """
                    
            dp=[0.0]*(K+W+1)
            dp[0]=1.0
            s=1.0
            for i in range(1, len(dp)):
                dp[i]=s/W
                if i>=W:
                    s-=dp[i-W]
                if i<K:
                    s+=dp[i]
            return min(1.0, sum(dp[i] for i in range(K, N+1)))