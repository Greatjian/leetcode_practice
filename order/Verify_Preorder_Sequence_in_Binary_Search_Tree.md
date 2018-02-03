# 255. Verify Preorder Sequence in Binary Search Tree

Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Follow up:
- Could you do it using only constant space complexity?

## Method:

divide and conquer, O(nlogn)~O(n^2), tle:

    class Solution(object):
        def verifyPreorder(self, preorder):
            """
            :type preorder: List[int]
            :rtype: bool
            """
            if not preorder or len(preorder)==1:
                return True
            i=0
            while i<len(preorder):
                if preorder[i]>preorder[0]:
                    break
                i+=1
            if any(preorder[j]<=preorder[0] for j in range(i+1, len(preorder))):
                return False
            return self.verifyPreorder(preorder[1:i]) and self.verifyPreorder(preorder[i:])
            
stack, O(n) space:

    class Solution(object):
        def verifyPreorder(self, preorder):
            """
            :type preorder: List[int]
            :rtype: bool
            """
            stack=[]
            low=float('-inf')
            for p in preorder:
                if p<low:
                    return False
                while stack and stack[-1]<p:
                    low=stack.pop()
                stack.append(p)
            return True
            
## Solution:

O(1) space:

    class Solution(object):
        def verifyPreorder(self, preorder):
            """
            :type preorder: List[int]
            :rtype: bool
            """
            low=float('-inf')
            i=-1
            for p in preorder:
                if p<low:
                    return False
                while i>=0 and preorder[i]<p:
                    low=preorder[i]
                    i-=1
                i+=1
                preorder[i]=p
            return True

