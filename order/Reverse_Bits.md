# 190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
- If this function is called many times, how would you optimize it?

Related problem: Reverse Integer

## Method:

类似reverse a integer:

    res=0
    while n:
        res=res*10+n%10
        n/=10
        
这里如下：

    class Solution:
        # @param n, an integer
        # @return an integer
        def reverseBits(self, n):
            res=0
            for i in range(32):
                res=res<<1
                res|=(n&1)
                n>>=1
            return res
            
## Solution:

optimization:

4个一组:

    class Solution:
        # @param n, an integer
        # @return an integer
        def reverseBits(self, n):
            res=0
            bits=[0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
            for i in range(8):
                res=res<<4
                res|=bits[n&0b1111]
                n>>=4
            return res
            
O(log(size of n)):

> abcdefgh--efghabcd--ghefcdab----hgfedcba

    class Solution:
        # @param n, an integer
        # @return an integer
        def reverseBits(self, n):
            n = (n >> 16) | (n << 16);
            n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8);
            n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4);
            n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2);
            n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1);
            return n
            
使用bin()(string):

    class Solution:
        # @param n, an integer
        # @return an integer
        def reverseBits(self, n):
            bins = bin(n)[2:]
            bins = bins[::-1]
            rev = bins + "0"*(32-len(bins))
            return int(rev, 2)