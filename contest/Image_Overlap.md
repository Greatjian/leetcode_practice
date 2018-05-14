# 835. Image Overlap

Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

    Input: A = [[1,1,0],
                [0,1,0],
                [0,1,0]]
           B = [[0,0,0],
                [0,1,1],
                [0,0,1]]
    Output: 3
    Explanation: We slide A to right by 1 unit and down by 1 unit.

Notes: 

- 1 <= A.length = A[0].length = B.length = B[0].length <= 30
- 0 <= A[i][j], B[i][j] <= 1

## Method:

    class Solution(object):
        def largestOverlap(self, A, B):
            """
            :type A: List[List[int]]
            :type B: List[List[int]]
            :rtype: int
            """
            c, d=[], []
            for i in range(len(A)):
                for j in range(len(A[0])):
                    if A[i][j]:
                        c.append((i, j))
                    if B[i][j]:
                        d.append((i, j))
            dict=collections.defaultdict(int)
            for i in c:
                for j in d:
                    dict[(j[0]-i[0], j[1]-i[1])]+=1
            return max(dict.values()) if dict else 0
            