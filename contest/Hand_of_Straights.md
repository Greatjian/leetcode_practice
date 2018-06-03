# 846. Hand of Straights

Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

Example 1:

    Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
    Output: true
    Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].

Example 2:

    Input: hand = [1,2,3,4,5], W = 4
    Output: false
    Explanation: Alice's hand can't be rearranged into groups of 4.
 
Note:

- 1 <= hand.length <= 10000
- 0 <= hand[i] <= 10^9
- 1 <= W <= hand.length

## Method:

O(N*max(N, W)/W):

    class Solution(object):
        def isNStraightHand(self, hand, W):
            """
            :type hand: List[int]
            :type W: int
            :rtype: bool
            """
            l=len(hand)
            if l%W:
                return False
            d=collections.Counter(hand)
            for _ in range(l/W):
                m=min(d.keys())
                for _ in range(W):
                    if d[m]>0:
                        d[m]-=1
                        if d[m]==0:
                            del d[m]
                        m+=1
                    else:
                        return False
            return d=={}
            
modify:

    class Solution(object):
        def isNStraightHand(self, hand, W):
            """
            :type hand: List[int]
            :type W: int
            :rtype: bool
            """
            l=len(hand)
            if l%W:
                return False
            d=collections.Counter(hand)
            for _ in range(l/W):
                m=min(d.keys())
                for _ in range(W):
                    if not d[m]:
                        return False
                    else:
                        d[m]-=1
                        if d[m]==0:
                            del d[m]
                    m+=1
            return d=={}
            
## Solution:

O(N), go through each number once:

    class Solution(object):
        def isNStraightHand(self, hand, W):
            """
            :type hand: List[int]
            :type W: int
            :rtype: bool
            """
            c = collections.Counter(hand)
            start = collections.deque()
            opened = 0
            for i in sorted(c):
                if opened > c[i]: return False
                if opened < c[i]: start.append([i, c[i] - opened])
                opened = c[i]
                if i == start[0][0] + W - 1: opened -= start.popleft()[1]
            return opened == 0