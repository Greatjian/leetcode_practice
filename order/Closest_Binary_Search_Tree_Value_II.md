# 272. Closest Binary Search Tree Value II

Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:
- Given target value is a floating point.
- You may assume k is always valid, that is: k ≤ total nodes.
- You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

Follow up:
- Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

## Method:

trivial O(nlgn)/ two pointers would be O(n):

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def closestKValues(self, root, target, k):
            """
            :type root: TreeNode
            :type target: float
            :type k: int
            :rtype: List[int]
            """
            res=[]
            
            def inorder(root):
                if not root:
                    return
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
                
            inorder(root)
            return sorted(res, key=lambda i: abs(i-target))[:k]

## Solution:
            
two stacks for small and large, getPrev() and getNext(), O(k+logn):

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def closestKValues(self, root, target, k):
            """
            :type root: TreeNode
            :type target: float
            :type k: int
            :rtype: List[int]
            """
            small, large, res = [], [], []
            self.initialize(root, small, large, target)
            for i in range(k):
                if not small:
                    res.append(self.getNext(large))
                elif not large:
                    res.append(self.getPrev(small))
                elif abs(large[-1].val-target)<abs(small[-1].val-target):
                    res.append(self.getNext(large))
                else:
                    res.append(self.getPrev(small))
            return res
            
            
        def initialize(self, root, small, large, target):
            while root:
                if root.val>target:
                    large.append(root)
                    root=root.left
                else:
                    small.append(root)
                    root=root.right
                    
        def getNext(self, large):
            root=large.pop()
            v=root.val
            root=root.right
            while root:
                large.append(root)
                root=root.left
            return v
            
        def getPrev(self, small):
            root=small.pop()
            v=root.val
            root=root.left
            while root:
                small.append(root)
                root=root.right
            return v