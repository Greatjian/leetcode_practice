# 859. Buddy Strings

Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B. 

Example 1:

    Input: A = "ab", B = "ba"
    Output: true

Example 2:

    Input: A = "ab", B = "ab"
    Output: false

Example 3:

    Input: A = "aa", B = "aa"
    Output: true

Example 4:

    Input: A = "aaaaaaabc", B = "aaaaaaacb"
    Output: true

Example 5:

    Input: A = "", B = "aa"
    Output: false
 
Note:

- 0 <= A.length <= 20000
- 0 <= B.length <= 20000
- A and B consist only of lowercase letters.

## Method:

1. check for empty
2. equals: check for duplicates
3. not equal: check for two non-identical part

- note: a more efficient way to check for duplicates:


    len(set(A)) < len(A)

implementation:

    class Solution(object):
        def buddyStrings(self, A, B):
            """
            :type A: str
            :type B: str
            :rtype: bool
            """
            if not A and not B:
                return False
            if A==B:
                return max(collections.Counter(A).values())>1
            if len(A)!=len(B):
                return False
            s=[i for i in range(len(A)) if A[i]!=B[i]]
            if len(s)!=2:
                return False
            i, j=s[0],s[1]
            return A[i]==B[j] and A[j]==B[i]