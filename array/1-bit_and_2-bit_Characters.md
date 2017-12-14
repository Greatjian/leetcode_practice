# 717. 1-bit and 2-bit Characters

We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:

    Input: 
    bits = [1, 0, 0]
    Output: True
    Explanation: 
    The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.

Example 2:

    Input: 
    bits = [1, 1, 1, 0]
    Output: False
    Explanation: 
    The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.

Note:

- 1 <= len(bits) <= 1000.
- bits[i] is always 0 or 1.

## Method:

iteration:

    class Solution(object):
        def isOneBitCharacter(self, bits):
            """
            :type bits: List[int]
            :rtype: bool
            """
            i=0
            while i<len(bits):
                if i==len(bits)-1:
                    return True
                if bits[i]==0:
                    i+=1
                else:
                    i+=2
            return False

recursion:

    class Solution(object):
        def isOneBitCharacter(self, bits):
            """
            :type bits: List[int]
            :rtype: bool
            """
            return self.helper(0, bits)
        
        def helper(self, idx, bits):
            if idx==len(bits)-1:
                return True
            if idx==len(bits):
                return False
            if bits[idx]==0:
                return self.helper(idx+1, bits)
            else:
                return self.helper(idx+2, bits)
                
deque:

    class Solution(object):
        def isOneBitCharacter(self, bits):
            """
            :type bits: List[int]
            :rtype: bool
            """
            d=collections.deque(bits)
            while d:
                if len(d)==1:
                    return True
                if d[0]==0:
                    d.popleft()
                else:
                    d.popleft()
                    d.popleft()
            return False
            
## Solution:

O(n) but in most cases faster:

    class Solution(object):
        def isOneBitCharacter(self, bits):
            """
            :type bits: List[int]
            :rtype: bool
            """
            i = len(bits) - 2
            while i >= 0:
                if bits[i] == 0:
                    break
                i -= 1
            return (len(bits) - i) % 2 == 0