# 187. Repeated DNA Sequences

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

    Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
    
    Return:
    ["AAAAACCCCC", "CCCCCAAAAA"].
    
## Method:

    class Solution(object):
        def findRepeatedDnaSequences(self, s):
            """
            :type s: str
            :rtype: List[str]
            """
            d=collections.defaultdict(int)
            for i in range(len(s)-9):
                d[s[i:i+10]]+=1
            return [i for i in d if d[i]>1]